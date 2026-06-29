import os
import requests
import sys

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
# Estructura de datos: 33ebbe69-b067-800c-918b-fa5349347cf3
PARENT_PAGE_ID = os.environ.get("PARENT_PAGE_ID", "33ebbe69-b067-800c-918b-fa5349347cf3")

if not NOTION_TOKEN:
    print("Error: NOTION_TOKEN not found.")
    sys.exit(1)

# Using the 2026 version that supports native Markdown
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2026-03-11"
}

def create_native_markdown_page(title, content, icon_emoji="📚"):
    url = "https://api.notion.com/v1/pages"
    
    # Payload using the 'markdown' parameter for perfect translation
    payload = {
        "parent": {"page_id": PARENT_PAGE_ID},
        "icon": {"type": "emoji", "emoji": icon_emoji},
        "cover": {"type": "external", "external": {"url": "https://www.notion.so/images/page-cover/rijksmuseum_jansz_1641.jpg"}},
        "properties": {
            "title": {"title": [{"text": {"content": title}}]}
        },
        "markdown": content
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Page created with native Markdown: {title}")
        return response.json()["id"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python upload_enhanced.py <title> <file_path> [icon]")
        sys.exit(1)
    
    title = sys.argv[1]
    file_path = sys.argv[2]
    icon = sys.argv[3] if len(sys.argv) > 3 else "📚"
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            create_native_markdown_page(title, content, icon)
    else:
        print(f"File not found: {file_path}")
