import argparse
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_uefi_spec(base_url, limit=None):
    print(f"Scraping UEFI spec from: {base_url}")
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching base URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'lxml')
    
    # The specification says we need to identify all links within the Table of Contents (ToC).
    # This is a bit heuristic as the exact ToC element might vary. 
    # We'll look for common patterns or assume the main content/nav contains it.
    # For now, let's try to find all links that are part of the spec structure.
    
    manifest = []
    
    # Heuristic: Look for a <nav> or a specific div that might contain the ToC.
    # In many UEFI specs, there is a side navigation or a main content area with links.
    # Let's try to find all links in the document and filter them.
    
    # For this implementation, we will assume the spec has a structure we can follow.
    # We'll look for links that are likely part of the specification chapters.
    
    links = soup.find_all('a', href=True)
    
    for link in links:
        if limit is not None and len(manifest) >= limit:
            break

        href = link['href']
        full_url = urljoin(base_url, href)
        title = link.get_text().strip()
        
        if not title or not full_url.startswith(base_url):
            continue
            
        # We need to determine hierarchy. This is complex without knowing the exact HTML structure.
        # A simple approach: use the path or some structural element.
        
        # Placeholder for hierarchy logic
        hierarchy = [title] 
        
        manifest.append({
            "title": title,
            "url": full_url,
            "hierarchy": hierarchy
        })

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Successfully created manifest.json with {len(manifest)} entries.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UEFI Spec Scraper")
    parser.add_argument("--url", required=True, help="Base URL of the UEFI specification")
    parser.add_argument("--limit", type=int, help="Limit the number of links to scrape")
    args = parser.parse_args()
    
    scrape_uefi_spec(args.url, limit=args.limit)

