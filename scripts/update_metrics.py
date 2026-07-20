"""
Auto-update citation metrics for the portfolio.
Primary source: Google Scholar (via `scholarly`).
Fallback: OpenAlex API (keyless, reliable from CI runners).

Writes: data/scholar_metrics.json  (consumed by the {{< metrics >}} shortcode)
Run from repo root:  python scripts/update_metrics.py
"""

import datetime
import json
import os
import sys

SCHOLAR_ID = "ryaF3dIAAAAJ"
ORCID = "0000-0002-1499-4646"
DATA_FILE = "data/scholar_metrics.json"


def from_scholar():
    from scholarly import scholarly  # imported lazily; may not be installed
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=["indices", "counts", "publications"])
    return {
        "pub_count": len(author.get("publications", [])),
        "citations": author.get("citedby", 0),
        "h_index": author.get("hindex", 0),
        "i10_index": author.get("i10index", 0),
        "source": "Google Scholar",
    }


def from_openalex():
    import urllib.request
    url = f"https://api.openalex.org/authors/orcid:{ORCID}"
    req = urllib.request.Request(url, headers={"User-Agent": "portfolio-metrics (mailto:vishalkotha1@gmail.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        a = json.load(r)
    stats = a.get("summary_stats", {})
    return {
        "pub_count": a.get("works_count", 0),
        "citations": a.get("cited_by_count", 0),
        "h_index": stats.get("h_index", 0),
        "i10_index": stats.get("i10_index", 0),
        "source": "OpenAlex",
    }


def load_previous():
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def main():
    metrics = None
    for name, fn in (("Google Scholar", from_scholar), ("OpenAlex", from_openalex)):
        try:
            print(f"Trying {name}...")
            metrics = fn()
            # Sanity check: never publish zeros over real data
            if metrics["citations"] and metrics["pub_count"]:
                print(f"OK from {name}: {metrics}")
                break
            print(f"{name} returned empty data, skipping.")
            metrics = None
        except Exception as e:
            print(f"{name} failed: {e}")
            metrics = None

    if metrics is None:
        prev = load_previous()
        if prev:
            print("All sources failed - keeping previous metrics unchanged.")
            sys.exit(0)
        print("All sources failed and no previous data exists.")
        sys.exit(1)

    # Guard against a source reporting fewer citations than we already have
    prev = load_previous()
    if prev and metrics["citations"] < prev.get("citations", 0) and metrics["source"] != prev.get("source"):
        print(f"New source ({metrics['source']}) reports fewer citations than existing "
              f"({metrics['citations']} < {prev['citations']}); keeping previous data.")
        sys.exit(0)

    metrics["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d")
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4)
    print(f"Saved {DATA_FILE}")


if __name__ == "__main__":
    main()
