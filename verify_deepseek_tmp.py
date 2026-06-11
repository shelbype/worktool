import json
import time
import urllib.request
body = json.dumps({'question': '设备平台要求'}, ensure_ascii=False).encode('utf-8')
req = urllib.request.Request('http://127.0.0.1:8000/rag/query', data=body, headers={'Content-Type':'application/json'}, method='POST')
start = time.time()
try:
    with urllib.request.urlopen(req, timeout=40) as resp:
        text = resp.read().decode('utf-8')
    elapsed = time.time() - start
    data = json.loads(text)
    print(json.dumps({
        'ok': True,
        'elapsed_seconds': round(elapsed, 3),
        'confidence': data.get('confidence'),
        'auto_reply': data.get('auto_reply'),
        'answer_preview': (data.get('answer') or '')[:240],
    }, ensure_ascii=False))
except Exception as exc:
    elapsed = time.time() - start
    print(json.dumps({'ok': False, 'elapsed_seconds': round(elapsed, 3), 'error': str(exc)}, ensure_ascii=False))