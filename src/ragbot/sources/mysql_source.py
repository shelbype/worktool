from __future__ import annotations

from datetime import datetime
from typing import Any
from urllib.parse import urlparse

import pymysql

from ragbot.domain import DocumentStatus, HelpDocument


class MySQLHelpDocumentSource:
    """Incremental MySQL reader for SaaS help-center documents.

    The default column names match the MVP schema assumption. Override
    `column_map` when the existing SaaS table uses different names.
    """

    DEFAULT_COLUMN_MAP = {
        "source_id": "id",
        "title": "title",
        "body_html": "body_html",
        "category": "category",
        "product_module": "product_module",
        "product_version": "product_version",
        "source_url": "source_url",
        "status": "status",
        "updated_at": "updated_at",
    }

    def __init__(self, dsn: str, table: str, column_map: dict[str, str] | None = None) -> None:
        self.dsn = dsn
        self.table = table
        self.column_map = {**self.DEFAULT_COLUMN_MAP, **(column_map or {})}

    def fetch_updated_since(self, since: datetime | None) -> list[HelpDocument]:
        columns = ", ".join(f"`{column}` AS `{field}`" for field, column in self.column_map.items())
        sql = f"SELECT {columns} FROM `{self.table}`"
        params: list[Any] = []
        if since is not None:
            sql += f" WHERE `{self.column_map['updated_at']}` > %s"
            params.append(since)
        sql += f" ORDER BY `{self.column_map['updated_at']}` ASC"

        connection = pymysql.connect(**self._connect_kwargs(), cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, params)
                rows = cursor.fetchall()
        finally:
            connection.close()
        return [self._row_to_document(row) for row in rows]

    def _connect_kwargs(self) -> dict[str, Any]:
        parsed = urlparse(self.dsn)
        if parsed.scheme not in {"mysql", "mysql+pymysql"}:
            raise ValueError("MYSQL_DSN must use mysql:// or mysql+pymysql://")
        return {
            "host": parsed.hostname or "localhost",
            "port": parsed.port or 3306,
            "user": parsed.username or "",
            "password": parsed.password or "",
            "database": parsed.path.lstrip("/"),
            "charset": "utf8mb4",
            "autocommit": True,
        }

    def _row_to_document(self, row: dict[str, Any]) -> HelpDocument:
        status = DocumentStatus.ACTIVE if row.get("status", "active") == "active" else DocumentStatus.ARCHIVED
        return HelpDocument(
            source_id=str(row["source_id"]),
            title=row["title"],
            body_html=row["body_html"],
            category=row.get("category"),
            product_module=row.get("product_module"),
            product_version=row.get("product_version"),
            source_url=row.get("source_url"),
            status=status,
            updated_at=row["updated_at"],
        )
