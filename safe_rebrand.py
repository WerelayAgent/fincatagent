import os
import re

filepath = r'C:\Tools\fincatagent\assets\index-DsrcOpJ6.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'"coming soon on pump\.fun"', '"coming soon on pons family"'),
    (r'"pump\.fun"', '"pons family"'),
    (r'https://pump\.fun', 'https://pons.family'),
    (r'"SPL memo · Solana"', '"SPL memo · Robinhood Chain"'),
    (r'" · Solana"', '" · Robinhood Chain"'),
    (r'"Solana"', '"Robinhood Chain"'),
    (r"'Solana'", "'Robinhood Chain'"),
    (r'"Phantom"', '"MetaMask"'),
    (r"'Phantom'", "'MetaMask'"),
    (r'install Phantom', 'install MetaMask'),
    (r'install phantom', 'install MetaMask'),
    (r'Solana address', 'Robinhood Chain address'),
    (r'Solana RPC', 'Robinhood Chain RPC'),
    (r'Solana Explorer', 'Robinhood Chain Explorer'),
    (r'signed to Solana', 'signed to Robinhood Chain'),
    (r'written to Solana', 'written to Robinhood Chain'),
    (r'writes that to Solana', 'writes that to Robinhood Chain'),
    (r'verdict to Solana', 'verdict to Robinhood Chain'),
    (r'verdicts to Solana', 'verdicts to Robinhood Chain'),
    (r'ask Solana', 'ask Robinhood Chain'),
    (r'committed to Solana', 'committed to Robinhood Chain'),
    (r'Solana error', 'Robinhood Chain error'),
    (r'Solana JSON-RPC', 'Robinhood Chain JSON-RPC')
]

for old, new in replacements:
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Safe replacements complete.")
