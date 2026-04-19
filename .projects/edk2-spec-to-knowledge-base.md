
# Project Specification: UEFI Spec-to-Knowledge-Base Pipeline

## 1. Project Overview
The goal of this project is to create an automated pipeline that scrapes the official UEFI specification (HTML format), converts it into structured, AI-ready Markdown files, and stores them in a versioned directory structure within GitHub. This allows for easy updates when new UEFI versions are released and provides a high-quality RAG (Retrieval-Augmented Generation) source for LLMs.

## 2. Technical Stack
- **Language:** Python 3.x
- **Scraping/Parsing:** `BeautifulSoup4`, `lxml`
- **Transformation Engine:** `Pandoc`
- **Automation:** GitHub Actions (`workflow_dispatch` trigger)
- **Data Format:** Markdown with YAML Frontmatter
- **Version Control:** Git

## 3. System Architecture

### A. The Scraper (`scripts/scraper.py`)
**Input:** A base URL of a UEFI specification (e.g., `https://uefi.org/specs/UEFI/2.11/`).
**Logic:**
1. Crawl the provided URL to identify all links within the Table of Contents (ToC).
2. Map the hierarchical relationship: Chapter $\rightarrow$ Section $\rightarrow$ Sub-section.
3. Extract the canonical URL for every identified section.
**Output:** A `manifest.json` file containing an array of objects:
```json
[
  {
    "title": "Chapter 7: Protocols",
    "url": "https://uefi.org/specs/UEFI/2.11/chapter7.html",
    "hierarchy": ["Chapter 7"]
  },
  ...
]
```

### B. The Transformer (`scripts/transformer.py`)
**Input:** `manifest.json` and the version number string.
**Logic:**
1. Iterate through every entry in `manifest.json`.
2. For each URL, execute a subprocess call to `pandoc`.
   - *Command Template:* `pandoc [URL] -f html -t markdown_strict -o [temp_output].md`
3. **Post-Processing:** Use BeautifulSoup to strip out HTML artifacts (e.g., `<nav>`, `<footer>`, `<script>`) that Pandoc might have missed.
4. **Metadata Injection:** Prepend a YAML frontmatter block to the top of every `.md` file.
**Output:** Structured `.md` files saved to `/specs/[version]/[chapter_name].md`.

**Required Markdown Format:**
```markdown
---
spec_version: "2.11"
hierarchy: ["Chapter 7", "Section 7.4"]
source_url: "https://uefi.org/specs/UEFI/2.11/chapter7.html"
last_updated: "YYYY-MM-DD"
---
# [Original Header]
[Converted Content]
```

### C. The Automation (`.github/workflows/update_spec.yml`)
**Trigger:** `workflow_dispatch` (Manual trigger via GitHub UI).
**Workflow Steps:**
1. **Setup:** Checkout repository, install Python and Pandoc on the runner.
2. **Execution:** 
   - Run `python scripts/scraper.py --url [USER_INPUT_URL]`.
   - Run `python scripts/transformer.py --version [USER_INPUT_VERSION]`.
3. **Commit:** Automatically commit and push the new `.md` files and updated `manifest.json` back to the repository.

## 4. Repository Structure
```text
├── .github/workflows/update_spec.yml
├── scripts/
│   ├── scraper.py
│   └── transformer.py
├── specs/
│   ├── v2.10/        <-- Archived versions
│   └── v2.11/        <-- Active version
├── manifest.json     <-- Generated mapping
└── requirements.txt
```

## 5. Implementation Instructions for AI (Copilot)
1. **Step 1:** Start by writing `requirements.txt` containing `beautifulsoup4`, `lxml`, and `jinja2`.
2. **Step 2:** Implement `scraper.py`. Focus on robustly parsing the HTML Table of Contents without including external links.
3. **Step 3:** Implement `transformer.py`. Ensure it handles the subprocess call to Pandoc correctly and implements the YAML frontmatter injection logic.
4. **Step 4:** Create the GitHub Action `.yml` file, ensuring it includes the `workflow_dispatch` input for `url` and `version`.

***

### How to use this with Copilot:
1.  **Create the file** in your repo as `project_plan.md`.
2.  **Open a new Python file** (e.g., `scraper.py`).
3.  **Highlight/Reference the plan** and type: 
    > *"Based on the requirements in project_plan.md, implement the scraper.py script."*
4.  **Repeat** for the transformer and the GitHub Action.