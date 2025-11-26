import re
from pathlib import Path



DSA_TOTAL_TARGET = 100

count = 0

ROOT = Path('../dsa')

# DSA counter
subfolders = [p for p in ROOT.iterdir() if p.is_dir()]

for subfolder in subfolders:
    for file in subfolder.iterdir():
        file = file.__str__()
        if file.endswith('.py') or file.endswith('.cpp'):
            count += 1

new_badge = f"### 100 (50 x 2) algorithm challenges ![](https://geps.dev/progress/{count})"

with open('../README.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r"### 100 \(50 x 2\) algorithm challenges !\[\]\(https://geps.dev/progress/\d+\)",
                 new_badge, content)

with open('../README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Progress updated: {count}/{DSA_TOTAL_TARGET}")





