from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from ragbot.audience import AUDIENCES, AudienceAssigner, AudienceRouter
from ragbot.config import Settings, get_settings
from ragbot.domain import ConfidenceLevel, HelpDocument, KnowledgeChunk, RetrievalResult
from ragbot.fast_answer import has_fast_answer_template
from ragbot.ingestion import IngestionService
from ragbot.providers import HashEmbeddingProvider, HttpEmbeddingProvider

from ragbot.quality_report import build_quality_report
from ragbot.repositories import InMemoryKnowledgeRepository, PostgresKnowledgeRepository
from ragbot.retrieval import RetrievalService
from ragbot.sources import HelpCenterXlsSource


def main() -> None:
    parser = argparse.ArgumentParser(prog="ragbot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_db = subparsers.add_parser("init-db")
    init_db.add_argument("--schema", default="db/init/001_schema.sql")

    import_helpcenter = subparsers.add_parser("import-helpcenter")
    import_helpcenter.add_argument("--source", default="db/init")
    import_helpcenter.add_argument("--clear", action="store_true")

    rebuild = subparsers.add_parser("rebuild-index")
    rebuild.add_argument("--source", default="db/init")

    init_audience = subparsers.add_parser("init-audience-indexes")
    init_audience.add_argument("--dimensions", type=int, default=None)

    rebuild_audience = subparsers.add_parser("rebuild-audience-index")
    rebuild_audience.add_argument("--source", default="db/init")

    inspect_audience = subparsers.add_parser("inspect-audience")
    inspect_audience.add_argument("--question", required=True)

    inspect_embedding = subparsers.add_parser("inspect-embedding")
    inspect_embedding.add_argument("--text", default="测试 embedding 维度")

    migrate_vector_dim = subparsers.add_parser("migrate-vector-dim")
    migrate_vector_dim.add_argument("--dimensions", type=int, default=None)

    migrate_index_type = subparsers.add_parser("migrate-index-type")

    eval_retrieval = subparsers.add_parser("eval-retrieval")
    eval_retrieval.add_argument("--cases", default="eval/questions.json")
    eval_retrieval.add_argument("--source", default="db/init")
    eval_retrieval.add_argument("--load-source", action="store_true")

    eval_routing = subparsers.add_parser("eval-routing")
    eval_routing.add_argument("--cases", default="eval/questions.json")

    eval_full = subparsers.add_parser("eval-full")
    eval_full.add_argument("--cases", default="eval/questions.json")
    eval_full.add_argument("--source", default="db/init")
    eval_full.add_argument("--load-source", action="store_true")
    eval_full.add_argument("--baseline", default="eval/baseline.json")
    eval_full.add_argument("--save-baseline", action="store_true")
    eval_full.add_argument("--tolerance", type=float, default=0.05)

    quality_report = subparsers.add_parser("quality-report")
    quality_report.add_argument("--limit", type=int, default=100)
    quality_report.add_argument("--top", type=int, default=10)

    args = parser.parse_args()
    settings = get_settings()
    repository = build_repository(settings)

    if args.command == "init-db":
        if not isinstance(repository, PostgresKnowledgeRepository):
            raise SystemExit("init-db requires REPOSITORY_PROVIDER=postgres")
        schema_sql = Path(args.schema).read_text(encoding="utf-8")
        repository.init_schema(schema_sql)
        print(json.dumps({"initialized": True, "schema": args.schema}, ensure_ascii=False))
        return

    if args.command == "import-helpcenter":
        result = import_helpcenter_documents(settings, repository, Path(args.source), clear=args.clear)
        print(json.dumps(result, ensure_ascii=False))
        return

    if args.command == "rebuild-index":
        result = import_helpcenter_documents(settings, repository, Path(args.source), clear=True)
        print(json.dumps(result, ensure_ascii=False))
        return

    if args.command == "init-audience-indexes":
        if not isinstance(repository, PostgresKnowledgeRepository):
            raise SystemExit("init-audience-indexes requires REPOSITORY_PROVIDER=postgres")
        dimensions = args.dimensions or settings.embedding_dimensions
        repository.init_audience_indexes(dimensions)
        print(json.dumps({"initialized": True, "dimensions": dimensions, "audiences": list(AUDIENCES)}, ensure_ascii=False))
        return

    if args.command == "rebuild-audience-index":
        result = rebuild_audience_index(settings, repository, Path(args.source))
        print(json.dumps(result, ensure_ascii=False))
        return

    if args.command == "inspect-audience":
        route = AudienceRouter(settings.audience_routing_path, settings.max_route_audiences).route(args.question)
        print(
            json.dumps(
                {
                    "question": args.question,
                    "audiences": route.audiences,
                    "confidence": route.confidence,
                    "reason": route.reason,
                    "scores": route.scores,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "inspect-embedding":
        provider = build_embedding_provider(settings)
        vector = provider.embed(args.text)
        result = {
            "provider": settings.embedding_provider,
            "model": settings.embedding_model if settings.embedding_provider == "http" else "hash",
            "configured_dimensions": settings.embedding_dimensions,
            "actual_dimensions": len(vector),
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.command == "migrate-vector-dim":
        if not isinstance(repository, PostgresKnowledgeRepository):
            raise SystemExit("migrate-vector-dim requires REPOSITORY_PROVIDER=postgres")
        dimensions = args.dimensions or settings.embedding_dimensions
        repository.migrate_embedding_dimension(dimensions)
        print(json.dumps({"migrated": True, "dimensions": dimensions}, ensure_ascii=False))
        return

    if args.command == "migrate-index-type":
        if not isinstance(repository, PostgresKnowledgeRepository):
            raise SystemExit("migrate-index-type requires REPOSITORY_PROVIDER=postgres")
        repository.migrate_index_type()
        print(json.dumps({"migrated": True, "index_type": settings.vector_index_type}, ensure_ascii=False))
        return

    if args.command == "eval-retrieval":
        if isinstance(repository, InMemoryKnowledgeRepository) or args.load_source:
            if settings.audience_routing_enabled:
                rebuild_audience_index(settings, repository, Path(args.source))
            else:
                import_helpcenter_documents(
                    settings,
                    repository,
                    Path(args.source),
                    clear=isinstance(repository, InMemoryKnowledgeRepository),
                )
        retrieval = RetrievalService(repository, build_embedding_provider(settings), settings)
        cases = load_eval_cases(Path(args.cases))
        result = evaluate_retrieval_cases(cases, retrieval)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.command == "eval-routing":
        cases = load_eval_cases(Path(args.cases))
        result = evaluate_routing_cases(
            cases,
            AudienceRouter(settings.audience_routing_path, settings.max_route_audiences),
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.command == "eval-full":
        result = run_eval_full(
            settings,
            repository,
            Path(args.cases),
            Path(args.source),
            Path(args.baseline),
            load_source=args.load_source,
            save_baseline=args.save_baseline,
            tolerance=args.tolerance,
        )
        report = result["report"]
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if not result["passed"]:
            raise SystemExit(1)
        return

    if args.command == "quality-report":
        logs = repository.list_conversations(args.limit)
        result = build_quality_report(logs, args.top)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return


def build_repository(settings: Settings):
    if settings.repository_provider == "postgres":
        return PostgresKnowledgeRepository(
            settings.postgres_dsn,
            vector_index_type=settings.vector_index_type,
            vector_index_m=settings.vector_index_m,
            vector_index_ef_construction=settings.vector_index_ef_construction,
            vector_index_ef_search=settings.vector_index_ef_search,
            vector_index_lists=settings.vector_index_lists,
        )
    return InMemoryKnowledgeRepository()


def build_embedding_provider(settings: Settings):
    if settings.embedding_provider == "http":
        return HttpEmbeddingProvider(
            settings.embedding_api_base or settings.llm_api_base,
            settings.embedding_api_key or settings.llm_api_key,
            settings.embedding_model,
            settings.embedding_dimensions,
            settings.embedding_encoding_format,
        )
    return HashEmbeddingProvider(settings.embedding_dimensions)


def import_helpcenter_documents(settings: Settings, repository, source_dir: Path, clear: bool = False) -> dict[str, int]:
    if clear and hasattr(repository, "clear_knowledge"):
        repository.clear_knowledge()
    source = HelpCenterXlsSource(source_dir)
    ingestion = IngestionService(build_embedding_provider(settings))
    documents = source.load_documents()
    total_chunks = 0
    total_images = 0
    for document in documents:
        chunks = ingestion.ingest_document(document)
        assign_deterministic_chunk_ids(document, chunks)
        repository.upsert_chunks(chunks)
        total_chunks += len(chunks)
        total_images += sum(len(chunk.image_refs) for chunk in chunks)
    return {
        "documents": len(documents),
        "chunks": total_chunks,
        "image_refs": total_images,
        "cleared": int(clear),
    }


def rebuild_audience_index(settings: Settings, repository, source_dir: Path) -> dict[str, object]:
    if isinstance(repository, PostgresKnowledgeRepository):
        repository.init_audience_indexes(settings.embedding_dimensions)
    if not hasattr(repository, "clear_audience_knowledge") or not hasattr(repository, "upsert_audience_chunks"):
        raise SystemExit("repository does not support audience indexes")
    repository.clear_audience_knowledge()
    source = HelpCenterXlsSource(source_dir)
    ingestion = IngestionService(build_embedding_provider(settings))
    assigner = AudienceAssigner(settings.audience_routing_path)
    documents = source.load_documents()
    documents_by_audience = {audience: 0 for audience in AUDIENCES}
    chunks_by_audience = {audience: 0 for audience in AUDIENCES}
    total_images = 0
    for document in documents:
        chunks = ingestion.ingest_document(document)
        assign_deterministic_chunk_ids(document, chunks)
        audiences = assigner.assign_document(document)
        total_images += sum(len(chunk.image_refs) for chunk in chunks)
        for audience in audiences:
            repository.upsert_audience_chunks(audience, chunks)
            documents_by_audience[audience] += 1
            chunks_by_audience[audience] += len(chunks)
    return {
        "documents": len(documents),
        "audiences": list(AUDIENCES),
        "documents_by_audience": documents_by_audience,
        "chunks_by_audience": chunks_by_audience,
        "image_refs": total_images,
        "cleared": 1,
    }


def assign_deterministic_chunk_ids(document: HelpDocument, chunks: list[KnowledgeChunk]) -> None:
    for index, chunk in enumerate(chunks):
        digest = hashlib.sha256(f"{document.source_id}:{index}".encode("utf-8")).hexdigest()
        chunk.id = f"chunk_{digest[:32]}"
        chunk.document_id = document.id


def load_eval_cases(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        raise SystemExit(f"eval cases not found: {path}")
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise SystemExit("eval cases must be a JSON array")
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict) or not case.get("question"):
            raise SystemExit(f"eval case #{index} must include question")
    return cases


def evaluate_retrieval_cases(cases: list[dict[str, object]], retrieval: RetrievalService) -> dict[str, object]:
    details: list[dict[str, object]] = []
    top1_hits = 0
    top3_hits = 0
    retrieval_cases = 0
    auto_correct = 0
    handoff_correct = 0
    false_auto_reply = 0

    for case in cases:
        question = str(case["question"])
        expected_keywords = [str(item) for item in case.get("expected_keywords", [])]
        expected_source_ids = [str(item) for item in case.get("expected_source_ids", [])]
        should_auto_reply = bool(case.get("should_auto_reply", False))
        should_handoff = bool(case.get("should_handoff", not should_auto_reply))
        result = retrieval.retrieve(question)
        top_titles = [hit.chunk.title for hit in result.hits[:3]]
        top_contents = [hit.chunk.effective_answer_content for hit in result.hits[:3]]
        top1_hit: bool | None = None
        top3_hit: bool | None = None
        if expected_keywords or expected_source_ids:
            retrieval_cases += 1
            top1_hit = _case_matches(expected_keywords, expected_source_ids, result.hits[:1])
            top3_hit = _case_matches(expected_keywords, expected_source_ids, result.hits[:3])
        actual_auto_reply = _would_auto_reply(question, result)
        actual_handoff = not actual_auto_reply

        top1_hits += int(top1_hit is True)
        top3_hits += int(top3_hit is True)
        auto_correct += int(actual_auto_reply == should_auto_reply)
        handoff_correct += int(actual_handoff == should_handoff)
        false_auto_reply += int(actual_auto_reply and not should_auto_reply)

        details.append(
            {
                "id": case.get("id", ""),
                "module": case.get("module", ""),
                "question": question,
                "requires_image": bool(case.get("requires_image", False)),
                "confidence": str(result.confidence),
                "confidence_score": round(result.confidence_score, 4),
                "top_titles": top_titles,
                "top_source_ids": [str(hit.chunk.metadata.get("source_id") or hit.chunk.document_id) for hit in result.hits[:3]],
                "top_audiences": [hit.audience for hit in result.hits[:3]],
                "routed_audiences": result.routed_audiences,
                "routing_confidence": result.routing_confidence,
                "top1_hit": top1_hit,
                "top3_hit": top3_hit,
                "expected_auto_reply": should_auto_reply,
                "actual_auto_reply": actual_auto_reply,
                "expected_handoff": should_handoff,
                "actual_handoff": actual_handoff,
            }
        )

    total = max(1, len(cases))
    retrieval_total = max(1, retrieval_cases)
    return {
        "total": len(cases),
        "retrieval_cases": retrieval_cases,
        "top1_hit_rate": round(top1_hits / retrieval_total, 4),
        "top3_hit_rate": round(top3_hits / retrieval_total, 4),
        "auto_reply_accuracy": round(auto_correct / total, 4),
        "handoff_accuracy": round(handoff_correct / total, 4),
        "false_auto_reply_count": false_auto_reply,
        "details": details,
    }


def evaluate_routing_cases(cases: list[dict[str, object]], router: AudienceRouter) -> dict[str, object]:
    details: list[dict[str, object]] = []
    evaluated = 0
    top1_hits = 0
    covered_hits = 0
    for case in cases:
        question = str(case["question"])
        expected = [str(item) for item in case.get("expected_audiences", []) if str(item) in AUDIENCES]
        route = router.route(question)
        top1_hit: bool | None = None
        covered_hit: bool | None = None
        if expected:
            evaluated += 1
            top1_hit = bool(route.audiences and route.audiences[0] in expected)
            covered_hit = any(audience in expected for audience in route.audiences)
            top1_hits += int(top1_hit)
            covered_hits += int(covered_hit)
        details.append(
            {
                "id": case.get("id", ""),
                "question": question,
                "expected_audiences": expected,
                "routed_audiences": route.audiences,
                "routing_confidence": route.confidence,
                "routing_reason": route.reason,
                "scores": route.scores,
                "top1_hit": top1_hit,
                "covered_hit": covered_hit,
            }
        )
    denominator = max(1, evaluated)
    return {
        "total": len(cases),
        "evaluated": evaluated,
        "top1_accuracy": round(top1_hits / denominator, 4),
        "covered_accuracy": round(covered_hits / denominator, 4),
        "details": details,
    }


def run_eval_full(
    settings: Settings,
    repository,
    cases_path: Path,
    source_path: Path,
    baseline_path: Path,
    *,
    load_source: bool = False,
    save_baseline: bool = False,
    tolerance: float = 0.05,
) -> dict[str, object]:
    """Run full evaluation (retrieval + routing) and compare against baseline.

    Returns {"passed": bool, "report": dict} with exit code 1 when any metric
    drops more than tolerance (default 5%) below baseline.
    """
    # Prepare repository with data if needed
    if isinstance(repository, InMemoryKnowledgeRepository) or load_source:
        if settings.audience_routing_enabled:
            rebuild_audience_index(settings, repository, source_path)
        else:
            import_helpcenter_documents(
                settings, repository, source_path,
                clear=isinstance(repository, InMemoryKnowledgeRepository),
            )

    retrieval = RetrievalService(repository, build_embedding_provider(settings), settings)
    cases = load_eval_cases(cases_path)

    retrieval_report = evaluate_retrieval_cases(cases, retrieval)
    routing_report = evaluate_routing_cases(
        cases,
        AudienceRouter(settings.audience_routing_path, settings.max_route_audiences),
    )

    current_metrics = {
        "top1_hit_rate": retrieval_report["top1_hit_rate"],
        "top3_hit_rate": retrieval_report["top3_hit_rate"],
        "auto_reply_accuracy": retrieval_report["auto_reply_accuracy"],
        "handoff_accuracy": retrieval_report["handoff_accuracy"],
        "false_auto_reply_count": retrieval_report["false_auto_reply_count"],
        "routing_top1_accuracy": routing_report["top1_accuracy"],
        "routing_covered_accuracy": routing_report["covered_accuracy"],
    }

    if save_baseline:
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline = {
            "description": "Baseline metrics for regression comparison.",
            "tolerance": tolerance,
            "metrics": current_metrics,
        }
        baseline_path.write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding="utf-8")
        return {
            "passed": True,
            "report": {
                "action": "saved_baseline",
                "baseline": str(baseline_path),
                "metrics": current_metrics,
                "retrieval_details": retrieval_report,
                "routing_details": routing_report,
            },
        }

    # Compare against baseline
    baseline = None
    if baseline_path.exists():
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        baseline_metrics = baseline.get("metrics", {})
    else:
        baseline_metrics = {}

    diffs: list[str] = []
    passed = True
    metric_keys = [
        ("top1_hit_rate", "Top-1 hit rate"),
        ("top3_hit_rate", "Top-3 hit rate"),
        ("auto_reply_accuracy", "Auto-reply accuracy"),
        ("handoff_accuracy", "Handoff accuracy"),
        ("routing_top1_accuracy", "Routing top-1 accuracy"),
        ("routing_covered_accuracy", "Routing covered accuracy"),
    ]

    for key, label in metric_keys:
        current = current_metrics.get(key, 0)
        baseline_val = baseline_metrics.get(key)
        if baseline_val is None:
            diffs.append(f"{label}: {current:.4f} (no baseline)")
            continue
        delta = current - baseline_val
        status = "PASS" if delta >= -tolerance else "FAIL"
        diffs.append(f"{label}: {current:.4f} vs {baseline_val:.4f} (delta={delta:+.4f}) [{status}]")
        if delta < -tolerance:
            passed = False

    # False auto-reply count: fail if increases
    false_auto = current_metrics.get("false_auto_reply_count", 0)
    baseline_false = baseline_metrics.get("false_auto_reply_count")
    if baseline_false is not None and false_auto > baseline_false:
        diffs.append(
            f"False auto-reply: {false_auto} vs {baseline_false} (+{false_auto - baseline_false}) [FAIL]"
        )
        passed = False

    return {
        "passed": passed,
        "report": {
            "action": "compare_baseline",
            "baseline": str(baseline_path),
            "passed": passed,
            "metrics": current_metrics,
            "diffs": diffs,
            "retrieval_details": retrieval_report,
            "routing_details": routing_report,
        },
    }


def _would_auto_reply(question: str, result: RetrievalResult) -> bool:
    if result.confidence == ConfidenceLevel.HIGH:
        return True
    return result.confidence == ConfidenceLevel.MEDIUM and has_fast_answer_template(question)


def _case_matches(expected_keywords: list[str], expected_source_ids: list[str], hits) -> bool:
    for hit in hits:
        source_id = str(hit.chunk.metadata.get("source_id") or hit.chunk.document_id)
        if expected_source_ids and source_id in expected_source_ids:
            return True
    if expected_keywords:
        text = "\n".join([hit.chunk.title for hit in hits] + [hit.chunk.effective_search_text for hit in hits])
        return any(keyword and keyword in text for keyword in expected_keywords)
    return False


if __name__ == "__main__":
    main()
