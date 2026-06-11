from ragbot.container import container
result = container.retrieval_service.retrieve('设备平台要求')
print('confidence', result.confidence, result.confidence_score)
urls = []
for hit in result.hits:
    for image in hit.chunk.image_refs:
        if image.url not in urls:
            urls.append(image.url)
print('image_count', len(urls))
for url in urls[:3]:
    print(url)