import json
import time
import urllib.request
for i in range(3):
    payload = {
        'spoken': '怎么新建班级',
        'rawSpoken': '@xclass AI 怎么新建班级',
        'receivedName': '测速用户',
        'groupName': '测试群',
        'groupRemark': '测试群',
        'roomType': 1,
        'atMe': 'true',
        'textType': 1,
        'messageId': f'latency-image-test-{int(time.time())}-{i}',
    }
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request('http://139.196.6.90:8000/worktool/qa', data=body, headers={'Content-Type':'application/json'}, method='POST')
    start = time.time()
    with urllib.request.urlopen(req, timeout=20) as resp:
        text = resp.read().decode('utf-8')
    elapsed = time.time() - start
    print(json.dumps({'run': i + 1, 'elapsed': round(elapsed, 3), 'preview': text[:180]}, ensure_ascii=False))