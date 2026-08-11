import os
import re

filepath = r'C:\Tools\fincatagent\assets\index-DsrcOpJ6.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Text changes
    (r'"no contract yet — pre-launch"', '"no contract yet — pre-launch on pons family"'),
    (r'" SOL"', '" ETH"'),
    (r'" SOL "', '" ETH "'),
    (r'"SOL"', '"ETH"'),
    (r'"size \(SOL\)"', '"size (ETH)"'),
    (r'"Size in SOL"', '"Size in ETH"'),
    (r'"SOL JUP BONK"', '"ETH JUP BONK"'),
    (r'"SOL / day"', '"ETH / day"'),
    
    # Wallet strings
    (r'"install phantom, solflare or backpack"', '"install metamask"'),
    (r'"install phantom"', '"install metamask"'),
    (r'"Phantom"', '"MetaMask"'),
    (r'"Solflare"', '"MetaMask"'),
    (r'"Backpack"', '"MetaMask"'),
    (r'https://phantom\.app', 'https://metamask.io'),
    (r'https://solflare\.com', 'https://metamask.io'),
]

for old, new in replacements:
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Safe round 2 replacements complete.")
