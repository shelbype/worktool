import json
import urllib.request
for url, body in [
    ('http://127.0.0.1:8000/rag/query', {'question': '设备平台要求'}),
    ('http://127.0.0.1:8000/worktool/qa', {
        'spoken': '怎么新建班级',
        'rawSpoken': '@xclass AI 怎么新建班级',
        'receivedName': '张老师',
        'groupName': '测试群',
        'groupRemark': '测试群',
        'roomType': 1,
        'atMe': 'true',
        'textType': 1,
        'messageId': 'postgres-after-restart-001',
    }),
]:
    data = json.dumps(body, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type':'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(url, resp.read().decode('utf-8')[:500])
with urllib.request.urlopen('http://127.0.0.1:8000/conversations?limit=3', timeout=10) as resp:
    print('conversations', resp.read().decode('utf-8')[:1000])