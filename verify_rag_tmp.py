import json
import urllib.request
queries = ['设备平台要求', '企业微信怎么用', '怎么新建班级', '合同报价怎么签']
for q in queries:
    body = json.dumps({'question': q}, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request('http://127.0.0.1:8000/rag/query', data=body, headers={'Content-Type':'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    print(json.dumps({
        'question': q,
        'confidence': data['confidence'],
        'score': data['confidence_score'],
        'auto_reply': data['auto_reply'],
        'needs_human': data['needs_human'],
        'answer': (data['answer'] or '')[:160],
    }, ensure_ascii=False))

payload = {
    'spoken': '设备平台要求',
    'rawSpoken': '@xclass AI 设备平台要求',
    'receivedName': '张老师',
    'groupName': '测试群',
    'groupRemark': '测试群',
    'roomType': 1,
    'atMe': 'true',
    'textType': 1,
    'messageId': 'postgres-worktool-test-003',
}
body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
req = urllib.request.Request('http://127.0.0.1:8000/worktool/qa', data=body, headers={'Content-Type':'application/json'}, method='POST')
with urllib.request.urlopen(req, timeout=10) as resp:
    print('worktool', resp.read().decode('utf-8')[:500])