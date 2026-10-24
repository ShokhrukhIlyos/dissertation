#!/usr/bin/env python3
"""
Knowledge Base Search Utility for AI Agents and Researchers.
Searches across the 33 academic psycholinguistics/linguistics texts in knowledge_base/.
"""

import os
import sys
import argparse
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
KB_DIR = os.path.join(ROOT_DIR, "knowledge_base")
CATALOG_PATH = os.path.join(ROOT_DIR, "catalog.json")

def load_catalog():
    if os.path.exists(CATALOG_PATH):
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            return json.load(f).get("documents", [])
    return []

def list_summary(docs):
    print("================================================================================")
    print("                     ACADEMIC KNOWLEDGE BASE SUMMARY                            ")
    print("================================================================================")
    print(f"Total Works Indexed: {len(docs)}\n")
    
    categories = {}
    for d in docs:
        cat = d.get("category", "unknown")
        categories.setdefault(cat, []).append(d)
        
    for cat, items in sorted(categories.items()):
        print(f"📁 {cat.upper()} ({len(items)} works):")
        for it in items:
            chars = it.get("char_count", 0)
            print(f"   - [{it['lang'].upper()}] {it['author']} ({it['year']}): {it['title']} ({chars:,} chars)")
        print()

def list_topics(docs):
    print("================================================================================")
    print("                     KNOWLEDGE BASE CORE TOPICS & ROUTING                       ")
    print("================================================================================")
    all_topics = {}
    for d in docs:
        for t in d.get("topics", []):
            all_topics.setdefault(t, []).append(f"{d['author']} ({d['year']}) -> {d['rel_path']}")
            
    for t in sorted(all_topics.keys()):
        print(f"🔹 {t}:")
        for ref in all_topics[t]:
            print(f"     • {ref}")
        print()

def search_content(query, docs, category_filter=None, lang_filter=None, max_results=10, context_lines=2):
    query_lower = query.lower()
    query_tokens = [tok for tok in re.split(r'\W+', query_lower) if len(tok) > 2]
    
    if not query_tokens:
        print("Query too short.")
        return

    results = []
    
    for doc_meta in docs:
        cat = doc_meta.get("category", "")
        lang = doc_meta.get("lang", "")
        
        if category_filter and category_filter.lower() not in cat.lower():
            continue
        if lang_filter and lang_filter.lower() != lang.lower():
            continue
            
        file_path = os.path.join(ROOT_DIR, doc_meta.get("rel_path", ""))
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
            
        doc_matches = []
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if query_lower in line_lower:
                score = 10
            else:
                matched_tokens = sum(1 for tok in query_tokens if tok in line_lower)
                score = matched_tokens if matched_tokens >= len(query_tokens) * 0.7 else 0
                
            if score > 0:
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                snippet = "".join(lines[start:end]).strip()
                doc_matches.append({
                    "line": i + 1,
                    "score": score,
                    "snippet": snippet
                })
                
        if doc_matches:
            # Sort matches by score descending
            doc_matches.sort(key=lambda x: x["score"], reverse=True)
            results.append({
                "meta": doc_meta,
                "matches": doc_matches
            })

    # Sort results by number of strong matches
    results.sort(key=lambda x: (len(x["matches"]), max(m["score"] for m in x["matches"])), reverse=True)
    
    print(f"Search Results for: '{query}' ({len(results)} matching documents)\n")
    displayed = 0
    for r in results:
        meta = r["meta"]
        print(f"📖 [{meta['lang'].upper()}] {meta['author']} ({meta['year']}) — {meta['title']}")
        print(f"   Path: {meta['rel_path']}")
        print(f"   Matches found: {len(r['matches'])}")
        for m in r['matches'][:3]:
            print(f"   --- Line {m['line']} (Score {m['score']}):")
            indented = "\n".join("     " + l for l in m["snippet"].splitlines())
            print(indented)
        print("=" * 80 + "\n")
        displayed += 1
        if displayed >= max_results:
            break

def main():
    parser = argparse.ArgumentParser(description="Search academic psycholinguistics knowledge base.")
    parser.add_argument("query", nargs="?", default="", help="Search query string or keywords")
    parser.add_argument("--category", "-c", help="Filter by category folder name (e.g., '01', 'speech', 'uzbek')")
    parser.add_argument("--lang", "-l", choices=["en", "ru", "uz"], help="Filter by language (en, ru, uz)")
    parser.add_argument("--limit", "-n", type=int, default=5, help="Maximum number of documents to return")
    parser.add_argument("--context", "-C", type=int, default=2, help="Context lines around matches")
    parser.add_argument("--summary", "-s", action="store_true", help="Print summary of entire knowledge base")
    parser.add_argument("--topics", "-t", action="store_true", help="List all indexed topics and key themes")

    args = parser.parse_args()
    docs = load_catalog()

    if args.summary:
        list_summary(docs)
    elif args.topics:
        list_topics(docs)
    elif args.query:
        search_content(args.query, docs, args.category, args.lang, args.limit, args.context)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

