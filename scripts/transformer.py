import json
import os
import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def transform_spec(manifest_path, output_base_dir, version="2.11"):
    if not os.path.exists(manifest_path):
        print(f"Error: {manifest_path} not found.")
        return

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    output_dir = os.path.join(output_base_dir, version)
    os.makedirs(output_dir, exist_ok=True)

    for entry in manifest:
        title = entry['title']
        url = entry['url']
        hierarchy = entry['hierarchy']
        
        # Create a filename-friendly title
        safe_title = "".join([c if c.isalnum() else "_" for c in title]).strip("_")
        file_path = os.path.join(output_dir, f"{safe_title}.md")

        print(f"Transforming: {title} -> {file_path}")

        try:
            # 1. Fetch HTML content
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text

            # Clean HTML to avoid Pandoc artifacts in Markdown
            soup = BeautifulSoup(html_content, 'html.parser')

            # Remove header links (anchor links)
            for a in soup.find_all('a', class_='headerlink'):
                a.decompose()

            # Remove problematic attributes that cause fenced divs in Pandoc output
            for tag in soup.find_all(True):
                for attr in ['itemscope', 'itemtype', 'role', 'itemprop']:
                    if tag.has_attr(attr):
                        del tag[attr]
                
                # Also remove the section-number span if it exists, to clean up headers
                if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    for span in tag.find_all('span', class_='section-number'):
                        span.unwrap()

            html_content = str(soup)

            # 2. Use pandoc to convert HTML to Markdown
            # We use a temporary file for the HTML input to avoid command line length limits
            temp_html = f"temp_{safe_title}.html"
            with open(temp_html, 'w', encoding='utf-8') as f:
                f.write(html_content)

            try:
                # Run pandoc command
                subprocess.run(['pandoc', temp_html, '-f', 'html', '-t', 'markdown', '-o', file_path], check=True)
            finally:
                if os.path.exists(temp_html):
                    os.remove(temp_html)

            # 3. Add YAML frontmatter and clean up
            with open(file_path, 'r', encoding='utf-8') as f:
                md_content = f.read()

            frontmatter = f"---\n"
            frontmatter += f"title: \"{title}\"\n"
            frontmatter += f"url: \"{url}\"\n"
            frontmatter += f"hierarchy: {json.dumps(hierarchy)}\n"
            frontcap_version = version
            frontmatter += f"version: \"{frontcap_version}\"\n"
            frontmatter += "---\n\n"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter + md_content)

        except Exception as e:
            print(f"Failed to transform {title}: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="UEFI Spec Transformer")
    parser.add_argument("--manifest", default="manifest.json", help="Path to manifest.json")
    parser.add_argument("--output-dir", default="specs", help="Base directory for output specs")
    parser.add_argument("--version", default="2.11", help="Spec version")
    args = parser.parse_args()

    transform_spec(args.manifest, args.output_dir, args.version)
