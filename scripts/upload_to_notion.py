import os
import re
import requests
import sys

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
PARENT_PAGE_ID = "33ebbe69-b067-800c-918b-fa5349347cf3"

if not NOTION_TOKEN:
    print("Error: NOTION_TOKEN not found in environment.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def md_to_notion_blocks(content):
    blocks = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Heading 1
        if line.startswith('# '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}
            })
        # Heading 2
        elif line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": line[3:]}}]}
            })
        # Heading 3
        elif line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": line[4:]}}]}
            })
        # Code block
        elif line.startswith('```'):
            lang = line[3:].strip() or "plain text"
            code_content = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_content.append(lines[i])
                i += 1
            blocks.append({
                "object": "block",
                "type": "code",
                "code": {
                    "rich_text": [{"type": "text", "text": {"content": '\n'.join(code_content)}}],
                    "language": lang if lang != "python" else "python"
                }
            })
        # Bullet list item
        elif line.startswith('- ') or line.startswith('* '):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}
            })
        # Paragraph
        elif line:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": line}}]}
            })
        i += 1
    return blocks

def create_notion_page(title, content):
    url = "https://api.notion.com/v1/pages"
    blocks = md_to_notion_blocks(content)
    
    # Split blocks into chunks of 100 (Notion API limit)
    # But since these are small files, we can probably fit them in one call.
    # Actually, the limit is 100 children per call.
    
    payload = {
        "parent": {"page_id": PARENT_PAGE_ID},
        "properties": {
            "title": {
                "title": [{"text": {"content": title}}]
            }
        },
        "children": blocks[:100] # Simple limit for now
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Successfully created page: {title}")
        return response.json()["id"]
    else:
        print(f"Error creating page {title}: {response.status_code}")
        print(response.text)
        return None

def main():
    clases = [
        ("Clase 1: Introducción", "Clase 1/clase1.md"),
        ("Clase 2: Funciones y Premisas", "Clase 2/clase2.md"),
        ("Clase 3: Notas", "Clase 3/clase3.md"),
        ("Clase 4: Estructuras", "Clase 4/clase4.md"),
        ("Clase 5: TDA y Objetos", "Clase 5/clase5.md"),
    ]
    
    for title, path in clases:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.strip():
                    create_notion_page(title, content)
                else:
                    print(f"Skipping empty file: {path}")
        else:
            print(f"File not found: {path}")

if __name__ == "__main__":
    main()
