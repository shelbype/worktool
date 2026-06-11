from ragbot.sources import HelpCenterXlsSource


def test_helpcenter_xls_source_reconstructs_documents():
    source = HelpCenterXlsSource("db/init")

    documents = source.load_documents()

    assert len(documents) == 141
    assert all(document.source_id.startswith("helpcenter:") for document in documents)
    assert all(document.title for document in documents)
    assert {document.category for document in documents} >= {"核心功能介绍", "初次使用指南", "热门问题"}


def test_helpcenter_xls_source_preserves_image_references():
    source = HelpCenterXlsSource("db/init")

    documents = source.load_documents()
    image_docs = [document for document in documents if document.image_urls]

    assert image_docs
    assert any("xiaosaas.oss-cn-beijing.aliyuncs.com" in url for doc in image_docs for url in doc.image_urls)
    assert any("<img " in doc.body_html for doc in image_docs)
