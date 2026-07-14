import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Text replacements
    content = re.sub(r'Finvo Agent', 'Fincat agent', content, flags=re.IGNORECASE)
    content = re.sub(r'Finvo', 'Fincat', content, flags=re.IGNORECASE)
    content = re.sub(r'FINVO', 'FINCAT', content, flags=re.IGNORECASE)
    content = re.sub(r'@finvoagent', '@fincatagent', content, flags=re.IGNORECASE)
    content = re.sub(r'finvo\.fun', 'fincatagent.com', content, flags=re.IGNORECASE)
    
    # Twitter link replacements
    content = re.sub(r'x\.com/finvoagent', 'x.com/fincatagent', content, flags=re.IGNORECASE)
    content = re.sub(r'twitter\.com/finvoagent', 'twitter.com/fincatagent', content, flags=re.IGNORECASE)
    
    # Wallet address -> coming soon on pump.fun
    content = content.replace('Gtq7iiDtzZQo5JEx6MEckW8PbRAfCc4T4vSsDNxHpump', 'coming soon on pump.fun')
    
    # Let's ensure FINCAT is capitalized properly if it was standalone
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.json', '.webmanifest')):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
