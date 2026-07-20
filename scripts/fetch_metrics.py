import json
import os
import sys
import datetime

# --- CONFIGURATION ---
AUTHOR_ID = 'ryaF3dIAAAAJ' # <--- Ensure this is set!
DATA_FILE = 'data/scholar_metrics.json'

try:
    from scholarly import scholarly
except ImportError:
    print("❌ ERROR: 'scholarly' library not found.")
    sys.exit(1)

def fetch_metrics():
    print(f"📊 Connecting to Google Scholar for ID: {AUTHOR_ID}...")
    
    try:
        # 1. Fetch Author Data (including publication list to count them)
        author = scholarly.search_author_id(AUTHOR_ID)
        scholarly.fill(author, sections=['indices', 'counts', 'publications']) 
        
        # 2. Extract Key Metrics
        metrics = {
            "pub_count": len(author.get("publications", [])), # Counts the papers
            "citations": author.get("citedby", 0),
            "h_index": author.get("hindex", 0),
            "i10_index": author.get("i10index", 0),
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d")
        }
        
        print(f"✅ Data Retrieved: {metrics['pub_count']} Pubs | {metrics['citations']} Citations")

        # 3. Save to Hugo Data Folder
        if not os.path.exists('data'):
            os.makedirs('data')
            
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(metrics, f, indent=4)
            
        print(f"💾 Saved dynamic metrics to {DATA_FILE}")

    except Exception as e:
        print(f"❌ Error fetching metrics: {e}")

if __name__ == "__main__":
    fetch_metrics()