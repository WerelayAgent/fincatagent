import os
import re

filepath = r'C:\Tools\fincatagent\assets\index-DsrcOpJ6.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'"\$Fincat"', '"$Fincat 0x79d21146370c3e5a453Cd20C752492275b415a3a"'),
    (r'"coming soon on pons family"', '"0x79d21146370c3e5a453Cd20C752492275b415a3a"'),
]

for old, new in replacements:
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("CA added successfully.")
