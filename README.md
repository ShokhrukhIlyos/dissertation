# Psycholinguistics, Cognitive Linguistics & Discourse Knowledge Base

An academic corpus and AI-ready Knowledge Base containing **33 foundational books, monographs, and research papers** across English, Russian, and Uzbek.

All source documents have been converted into clean, structured, and searchable Markdown (`.md`), accompanied by original source PDFs/DOCXs, deep machine-readable metadata (`catalog.json`), an interactive search tool (`search_kb.py`), and a dedicated AI agent instruction guide (`AI_KNOWLEDGE_BASE_GUIDE.md`).

---

## 📁 Repository Structure

```
Opam/
├── README.md                      # Knowledge Base entry point & quickstart
├── CATALOG.md                     # Human-readable table of all 33 indexed works
├── catalog.json                   # Machine-readable JSON manifest with deep metadata & topics
├── AI_KNOWLEDGE_BASE_GUIDE.md     # Specialized system prompt and routing guide for AI/LLMs
├── search_kb.py                   # Fast Python CLI full-text & semantic search utility
│
├── knowledge_base/                # Structured Markdown Knowledge Base
│   ├── 01_foundations_psycholinguistics/      # Leontiev, Zalevskaya, Pishchalnikova, Kess
│   ├── 02_speech_production_and_cognition/    # Levelt, Bergen, Ilyosov (Strategic Communication)
│   ├── 03_discourse_and_comprehension/        # Kintsch, Van Dijk, Zwaan & Radvansky
│   ├── 04_psychopoetics_and_narrative/        # Belyanin, Oatley, Green & Appel, Mar
│   ├── 05_text_analysis_and_stylistics/       # Bolotnova (Philological text analysis)
│   └── 06_uzbek_linguistics_and_pragmatics/   # Safarov, Azimova, Shamsieva, Abuzalova, Anvarova
│
└── source_documents/              # Archived original source files
    ├── pdf/                       # 32 original PDFs
    └── docx/                      # Original DOCX research material
```

---

## ⚡ Quickstart: Searching the Knowledge Base

A Python search utility is included in the root folder to query text, locate concepts, and extract snippets across the entire library:

```bash
# 1. Search for a term across all documents
python search_kb.py "situation model"

# 2. Search inside a specific thematic category
python search_kb.py "интерфейсная теория" --category 01

# 3. Filter by language (en, ru, uz)
python search_kb.py "концепт" --lang uz

# 4. View summary of all works and character counts
python search_kb.py --summary

# 5. Explore all indexed theoretical topics
python search_kb.py --topics
```

---

## 📚 Categorized Works Overview

### 1. Foundations of Psycholinguistics (`01_foundations_psycholinguistics`)
- **А. А. Леонтьев (2008):** *Основы психолингвистики* (Полное издание, 288 с.)
- **А. А. Леонтьев (2008):** *Основы психолингвистики* (Фрагмент / Вводные главы)
- **А. А. Леонтьев (1969):** *Язык, речь, речевая деятельность* (214 с.)
- **А. А. Залевская (1999):** *Введение в психолингвистику* (382 с.)
- **А. А. Залевская (2015):** *Что там – за словом? Вопросы интерфейсной теории значения слова*
- **В. А. Пищальникова (2021):** *История и теория психолингвистики*
- **В. А. Пищальникова (2023):** *Теоретические вопросы лингвистики эмоций*
- **Joseph F. Kess (1992):** *Psycholinguistics: Psychology, Linguistics, and the Study of Natural Language*

### 2. Speech Production and Cognition (`02_speech_production_and_cognition`)
- **Willem J. M. Levelt (1989):** *Speaking: From Intention to Articulation* (The MIT Press, 584 p.)
- **Benjamin K. Bergen (2012):** *Louder Than Words: The New Science of How the Mind Makes Meaning* (345 p.)
- **Shohruh Ilyosov (2024):** *COM501: When Communication Fails — Rio Tinto and Juukan Gorge Case Study*

### 3. Discourse and Comprehension (`03_discourse_and_comprehension`)
- **Walter Kintsch (1998):** *Comprehension: A Paradigm for Cognition* (486 p.)
- **Teun A. van Dijk & Walter Kintsch (1983):** *Strategies of Discourse Comprehension* (389 p.)
- **Rolf A. Zwaan & Gabriel A. Radvansky (1998):** *Situation Models in Language Comprehension and Memory*

### 4. Psychopoetics and Narrative (`04_psychopoetics_and_narrative`)
- **Melanie C. Green & Markus Appel (2024):** *Narrative Transportation: How Stories Shape How We See Ourselves and the World*
- **Keith Oatley (1999):** *Why Fiction May Be Twice as True as Fact: Fiction as Cognitive and Emotional Simulation*
- **Keith Oatley, Raymond A. Mar, Maja Djikic (2009):** *The Psychology of Fiction: Present and Future*
- **Raymond A. Mar (2018):** *Neuropsychological Studies of Narrative*
- **В. П. Белянин (1988):** *Психолингвистические аспекты художественного текста* (Изд-во МГУ)
- **Валерий Белянин (1996/2006):** *Введение в психиатрическое литературоведение* (281 с.)
- **В. П. Белянин (2006):** *Психологическое литературоведение: Текст как отражение внутренних миров автора и читателя*
- **Валерий Белянин (2000):** *Основы психолингвистической диагностики: Модели мира в литературе* (248 с.)

### 5. Text Analysis and Stylistics (`05_text_analysis_and_stylistics`)
- **Н. С. Болотнова (2009):** *Филологический анализ текста* (520 с.)

### 6. Uzbek Linguistics and Pragmatics (`06_uzbek_linguistics_and_pragmatics`)
- **Шаҳриёр Сафаров (2008):** *Прагмалингвистика* (318 бет)
- **Шаҳриёр Сафаров (2006):** *Когнитив тилшунослик* (92 бет)
- **Ирода Азимова (2008):** *Ўзбек тилидаги газета матнлари мазмуний перцепциясининг психолингвистик тадқиқи* (160 бет)
- **Манзура Бабабековна Шамсиева (2019):** *Билингвал болалар нутқининг психолингвистик тадқиқи*
- **М. К. Абузалова, Л. Б. Авлиёқулова (2024):** *Бадиий матннинг психолингвистик хусусиятлари*
- **Д. С. Худойберганова (2022):** *Миллий тилшунослигимиз тараққиётида антропоцентрик парадигманинг ўрни*
- **Илмий мақола (2024):** *Ўткир Ҳошимовнинг «Дунёнинг ишлари» қиссаси матнининг психолингвистик таҳлили*
- **Наргиза Мусулманова (2023):** *Лингвопоэтика*
- **Фарангиз Анварова (2025):** *Далолатнома: Илмий натижаларни амалиётга татбиқ этиш тўғрисида (PhD)*

---

## 🤖 Instructions for AI Agents & LLMs

Consult [`AI_KNOWLEDGE_BASE_GUIDE.md`](AI_KNOWLEDGE_BASE_GUIDE.md) for detailed routing instructions, cross-linguistic terminology maps (EN-RU-UZ), and citation standards.

