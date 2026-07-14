import os
import requests
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

BASE_URL = "https://finvo.fun/"
OUTPUT_DIR = "."

def download_file(url, local_path):
    # Clean query strings from local path
    local_path = local_path.split('?')[0]
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if os.path.exists(local_path):
        return
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {local_path}")
        return local_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def scrape_site():
    print(f"Scraping {BASE_URL}...")
    response = requests.get(BASE_URL)
    response.raise_for_status()
    html_content = response.text
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    soup = BeautifulSoup(html_content, "html.parser")
    assets_to_download = set()
    
    # 1. Find all resources in HTML
    for tag in soup.find_all(['link', 'script', 'img', 'meta']):
        url = tag.get('href') or tag.get('src') or tag.get('content')
        if url and (url.startswith('/') or url.startswith('./')):
            parsed = urlparse(url)
            clean_url = parsed.path
            full_url = urljoin(BASE_URL, url)
            local_path = "." + clean_url
            assets_to_download.add((full_url, local_path))

    # Download initial assets and collect JS/CSS files for deep scanning
    text_files = []
    for url, local_path in assets_to_download:
        dl = download_file(url, local_path)
        if dl and dl.endswith(('.js', '.css')):
            text_files.append(dl)
            
    # 2. Deep scan Vite CSS and JS chunks for extra assets
    asset_regex = re.compile(r'(/assets/[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+)')
    
    extra_assets = set()
    for text_file in text_files:
        try:
            with open(text_file, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = asset_regex.findall(content)
            for m in matches:
                full_url = urljoin(BASE_URL, m)
                local_path = "." + m
                extra_assets.add((full_url, local_path))
        except Exception:
            pass

    for url, local_path in extra_assets:
        download_file(url, local_path)
        
    print("Scraping completed.")

if __name__ == "__main__":
    scrape_site()
