# --- IMPORTS (Do not remove) ---
import os
import re
import datetime
import sys

# Try importing the library and handle the error if it's missing
try:
    from scholarly import scholarly
except ImportError:
    print("❌ ERROR: The 'scholarly' library is not installed.")
    print("   Please run: pip install scholarly")
    sys.exit(1)

# --- CONFIGURATION ---
# 1. Go to your Google Scholar profile
# 2. Look at the URL: https://scholar.google.com/citations?user=xY7z_AAAAJ&hl=en
# 3. Copy ONLY the part after user= (e.g., xY7z_AAAAJ)
AUTHOR_ID = 'ryaF3dIAAAAJ'  # <--- PASTE YOUR ID INSIDE THE QUOTES
OUTPUT_DIR = 'content/publication'

def slugify(text):
    """Cleans up the title for filenames"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text.strip('-')

def fetch_publications():
    print("------------------------------------------------")
    print("   SCIENTIFIC PORTFOLIO AUTOMATION SYSTEM       ")
    print("------------------------------------------------")
    
    if AUTHOR_ID == 'Put_Your_ID_Here':
        print("❌ NameError FIX: You forgot to replace 'Put_Your_ID_Here' with your actual ID in line 19.")
        return

    print(f"🔍 Connecting to Google Scholar for ID: {AUTHOR_ID}...")

    try:
        # Fetch the author profile
        author = scholarly.search_author_id(AUTHOR_ID)
        print(f"✅ Connection Successful! Found Author: {author.get('name', 'Unknown')}")
        
        # Fill the publications section
        print("⏳ Downloading publication list (this may take a minute)...")
        scholarly.fill(author, sections=['publications'])
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        print("   Hint: Check your internet connection or verify your Google Scholar ID.")
        return

    # Process publications
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    count = 0
    for pub in author['publications']:
        try:
            title = pub['bib']['title']
            slug = slugify(title)
            folder_path = os.path.join(OUTPUT_DIR, slug)
            file_path = os.path.join(folder_path, 'index.md')

            # Skip if already exists
            if os.path.exists(file_path):
                continue

            # Create folder
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Get Year
            year = pub['bib'].get('pub_year', datetime.datetime.now().year)
            
            # Write File
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"date: {year}-01-01\n")
                f.write(f"publishDate: {year}-01-01\n")
                f.write(f"publication: \"{pub['bib'].get('citation', 'Journal Article')}\"\n")
                f.write(f"authors: [\"Vishal Kotha\"]\n")
                f.write(f"---\n")
            
            print(f"   + Created: {title[:40]}...")
            count += 1

        except Exception as inner_e:
            print(f"   ! Skipped a paper due to data error: {inner_e}")
            continue

    print(f"\n🎉 SUCCESS: Added {count} new publications to your website.")

if __name__ == "__main__":
    fetch_publications()