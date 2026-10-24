# Testing the Knowledge Base

This guide explains how to check that the Knowledge Base is complete and consistent and that the search tool (`search_kb.py`) works. Run these checks after you add, rename, or remove a document, or after you edit `catalog.json`.

There is no test framework to install. Everything below runs with plain **Python 3.8+**.

---

## 1. Requirements

```bash
python --version          # Python 3.8 or newer
git lfs install           # only needed for section 5 (original PDFs)
```

Run every command from the repository root (the folder that contains `search_kb.py`).

---

## 2. Quick smoke test

These commands should run without errors and print results:

```bash
python search_kb.py --summary
python search_kb.py --topics
python search_kb.py "situation model"
```

| Command | Expected result |
|---|---|
| `--summary` | `Total Works Indexed: 33`, grouped into 6 category folders |
| `--topics` | A list of indexed topics (about 148), each with its documents |
| `"situation model"` | `8 matching documents`, with Kintsch (1998) first |

---

## 3. Search tool test cases

| # | What is tested | Command | Expected result |
|---|---|---|---|
| 1 | Plain English search | `python search_kb.py "situation model"` | 8 matching documents |
| 2 | Category filter | `python search_kb.py "интерфейсная теория" --category 01` | 1 matching document (Zalevskaya, folder 01) |
| 3 | Language filter | `python search_kb.py "концепт" --lang uz` | 2 matching documents, all `[UZ]` |
| 4 | Result limit | `python search_kb.py "lemma" --lang en -n 2` | No more than 2 documents shown |
| 5 | Context lines | `python search_kb.py "lemma" -C 0` | Each snippet is a single line |
| 6 | Query too short | `python search_kb.py "ab"` | Prints `Query too short.` |
| 7 | No matches | `python search_kb.py "zzqxnotaword"` | `0 matching documents` |
| 8 | Invalid language | `python search_kb.py "x" --lang fr` | Error: `invalid choice: 'fr' (choose from 'en', 'ru', 'uz')` |
| 9 | No arguments | `python search_kb.py` | Prints the help/usage text |
| 10 | Cyrillic / Uzbek text | `python search_kb.py "нутқ" --lang uz` | Results print correctly, without garbled characters |

> **Note:** If you pipe the output into `head` (for example `python search_kb.py --summary | head`), Python may print a `BrokenPipeError`. This is harmless: `head` closed the pipe early. It is not a bug in the script.

---

## 4. Catalog integrity check

This script checks that `catalog.json`, the Markdown files, and the source files all agree. Save it outside the repository (for example as `check_kb.py` in a temporary folder) and run it with the repository path:

```bash
python /path/to/check_kb.py .
```

```python
import json, os, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
cat = json.load(open(os.path.join(root, "catalog.json"), encoding="utf-8"))
docs = cat["documents"]
errors = []

if cat.get("total_documents") != len(docs):
    errors.append(f"total_documents={cat.get('total_documents')} but {len(docs)} entries")

required = ["id", "file", "category", "source", "author", "year",
            "lang", "title", "topics", "rel_path", "char_count"]
ids = set()
for d in docs:
    for k in required:
        if k not in d:
            errors.append(f"{d.get('id', '?')}: missing '{k}'")
    if d.get("id") in ids:
        errors.append(f"duplicate id {d['id']}")
    ids.add(d.get("id"))
    if d.get("lang") not in ("en", "ru", "uz"):
        errors.append(f"{d.get('id')}: bad lang {d.get('lang')}")
    p = os.path.join(root, d.get("rel_path", ""))
    if not os.path.isfile(p):
        errors.append(f"{d.get('id')}: missing file {d.get('rel_path')}")
        continue
    if os.path.getsize(p) == 0:
        errors.append(f"{d.get('id')}: empty file")
    sources = [os.path.join(root, "source_documents", s, d.get("source", "")) for s in ("pdf", "docx")]
    if not any(os.path.isfile(s) for s in sources):
        errors.append(f"{d.get('id')}: source {d.get('source')} not found")

# Every Markdown file in knowledge_base/ must be listed in the catalog
listed = {d["rel_path"] for d in docs}
for dp, _, fs in os.walk(os.path.join(root, "knowledge_base")):
    for f in fs:
        rel = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/")
        if f.endswith(".md") and rel not in listed:
            errors.append(f"not in catalog: {rel}")

print(f"{len(docs)} catalog entries checked")
for e in errors:
    print("FAIL:", e)
print("OK" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
```

**Expected output:**

```
33 catalog entries checked
OK
```

What it checks:

- `total_documents` matches the number of entries
- Every entry has all required fields, a unique `id`, and a valid language (`en`, `ru`, `uz`)
- Every `rel_path` points to an existing, non-empty Markdown file
- Every `source` exists in `source_documents/pdf/` or `source_documents/docx/`
- Every `.md` file in `knowledge_base/` is listed in the catalog (nothing is left out of search)

---

## 5. Original source files (Git LFS)

The PDFs in `source_documents/pdf/` are stored with **Git LFS**. If you cloned the repository without LFS, each PDF is only a small text placeholder. Check this with:

```bash
git lfs ls-files                    # should list 32 PDFs
head -c 100 source_documents/pdf/22.pdf
```

- If the output starts with `version https://git-lfs.github.com/spec/v1`, the file is a placeholder. Run `git lfs pull` to download the real PDFs.
- If the output starts with `%PDF`, the real file is present.

The Markdown files and the search tool **do not need** the PDFs. They work either way.

---

## 6. Manual documentation checks

When you change documents, also check these by hand:

- [ ] The number of works in `README.md`, `CATALOG.md`, `AI_KNOWLEDGE_BASE_GUIDE.md`, and `catalog.json` is the same
- [ ] Each new document appears in the correct category folder and in `CATALOG.md`
- [ ] Links in `CATALOG.md` open on GitHub. Relative paths such as `knowledge_base/...` work; local paths such as `file:///E:/...` do not
- [ ] No document is included twice

### Known issues (as of the last check)

- Links in `CATALOG.md` use local Windows paths (`file:///E:/Opam/...`) and do not work on GitHub.
- `heb08442.0001.001.md` and `levelt_willem_jm_speaking_from_intention_to_articulation.md` (folder 02) are identical copies of Levelt (1989).

---

## 7. Checklist after adding a new document

1. Put the original file in `source_documents/pdf/` or `source_documents/docx/`.
2. Put the Markdown version in the correct `knowledge_base/0X_.../` folder.
3. Add an entry to `catalog.json` and increase `total_documents`.
4. Add a row to `CATALOG.md` and update the README and the AI guide.
5. Run the integrity check (section 4). It should print `OK`.
6. Search for a phrase from the new document (section 3) and check that it is found.
