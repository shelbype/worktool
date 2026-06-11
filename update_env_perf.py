from pathlib import Path
path = Path('/home/admin/worktool/.env')
updates = {
    'MAX_LLM_CONTEXT_CHARS': '1600',
    'LLM_MAX_TOKENS': '320',
    'REPLY_IMAGES_ENABLED': 'true',
    'MAX_REPLY_IMAGES': '2',
}
lines = path.read_text().splitlines()
seen = set()
out = []
for line in lines:
    if '=' not in line or line.lstrip().startswith('#'):
        out.append(line)
        continue
    key = line.split('=', 1)[0]
    if key in updates:
        out.append(f'{key}={updates[key]}')
        seen.add(key)
    else:
        out.append(line)
for key, value in updates.items():
    if key not in seen:
        out.append(f'{key}={value}')
path.write_text('\n'.join(out) + '\n')