# AI Agent Guide: Psycholinguistics & Discourse Knowledge Base

This guide instructs AI models (ChatGPT, Claude, Gemini, Antigravity, local LLMs) on how to navigate, query, synthesize, and cite the academic texts stored in this knowledge base.

---

## 1. Scope & Theoretical Frameworks

This Knowledge Base houses **33 comprehensive academic works** spanning foundational and cutting-edge research across three primary linguistic traditions:
1. **Western Cognitive Psycholinguistics & Discourse Comprehension**:
   - Levelt’s Speech Production Model (Blueprint of the Speaker)
   - Kintsch’s Construction-Integration (CI) Model & Situation Models
   - Van Dijk & Kintsch’s Cognitive Discourse Macrostructures
   - Bergen’s Embodied Simulation Theory
   - Zwaan & Radvansky’s Event-Indexing Model
   - Narrative Transportation (Green & Appel) & Fiction Simulation (Oatley, Mar)
2. **Russian Psycholinguistic & Psychosemantic Tradition**:
   - Moscow Psycholinguistic School & Activity Theory (A. A. Leontiev)
   - Mental Lexicon & Interface Theory of Word Meaning (A. A. Zalevskaya)
   - Linguistic Emotiology & Theory of Emotion (V. A. Pishchalnikova, V. I. Shakhovsky)
   - Psychiatric Poetics & Emotional-Semantic Dominants in Text (V. P. Belyanin)
   - Philological Text Analysis & Communicative Stylistics (N. S. Bolotnova)
3. **Uzbek Linguistics, Pragmatics & Sociolinguistics**:
   - Pragmalinquistics & Speech Act Theory in Uzbek (Sh. Safarov)
   - Cognitive Linguistics & Concept Categorization (Sh. Safarov)
   - Media Discourse & Text Perception (I. Azimova)
   - Child Bilingualism & Ontogenesis (M. Shamsieva)
   - Uzbek Literary Text Poetics & Lingvopoetics (M. Abuzalova, L. Avliyoqulova, D. Xudoyberganova, N. Musulmanova)

---

## 2. Directory Layout & Routing Map

When an incoming query addresses a specific concept, route your search immediately to the corresponding category folder:

| Query Focus / Concept | Category Directory | Recommended Key Authors / Texts |
| :--- | :--- | :--- |
| **Speech Production**, Lemmas, Articulation, Monitoring | `knowledge_base/02_speech_production_and_cognition/` | Levelt (1989) (`heb08442.0001.001.md`) |
| **Embodied Cognition**, Motor Simulation, Brain & Language | `knowledge_base/02_speech_production_and_cognition/` | Bergen (2012) (`Benjamin_K_Bergen_...md`) |
| **Corporate / Strategic Communication Failure** | `knowledge_base/02_speech_production_and_cognition/` | Ilyosov (2024) (`When Communication Fails...md`) |
| **Discourse Comprehension**, CI Model, Working Memory | `knowledge_base/03_discourse_and_comprehension/` | Kintsch (1998) (`Kintsch - 1998...md`) |
| **Macrostructures**, Local Coherence, Text Strategies | `knowledge_base/03_discourse_and_comprehension/` | Van Dijk & Kintsch (1983) (`Teun_A_van_Dijk_...md`) |
| **Situation Models**, Event-Indexing Model (Time, Space) | `knowledge_base/03_discourse_and_comprehension/` | Zwaan & Radvansky (1998) (`situation_models_...md`) |
| **Narrative Transportation**, Story Immersion, Persuasion | `knowledge_base/04_psychopoetics_and_narrative/` | Green & Appel (2024) (`Green___Appel...md`) |
| **Fiction as Simulation**, Theory of Mind, Empathy | `knowledge_base/04_psychopoetics_and_narrative/` | Oatley (1999), Oatley et al. (2009), Mar (2018) |
| **Psychiatric Poetics**, Emotional Dominants (Светлые/Темные) | `knowledge_base/04_psychopoetics_and_narrative/` | Belyanin (1988, 1996, 2000, 2006) |
| **Activity Theory of Language**, Речевая деятельность | `knowledge_base/01_foundations_psycholinguistics/` | Leontiev (1969, 2008) |
| **Mental Lexicon**, Ассоциативные поля, Interface Theory | `knowledge_base/01_foundations_psycholinguistics/` | Zalevskaya (1999, 2015) |
| **History of Psycholinguistics**, Generations of Schools | `knowledge_base/01_foundations_psycholinguistics/` | Pishchalnikova (2021), Kess (1992) |
| **Linguistics of Emotions**, Эмоциология, Вербализация эмоций | `knowledge_base/01_foundations_psycholinguistics/` | Pishchalnikova (2023) |
| **Philological Analysis**, Цельность/Связность, Регулятивность | `knowledge_base/05_text_analysis_and_stylistics/` | Bolotnova (2009) |
| **Uzbek Pragmatics**, Нутқ актлари, Пресуппозиция | `knowledge_base/06_uzbek_linguistics_and_pragmatics/` | Safarov (2008) (`Pragmalingvistika...md`) |
| **Uzbek Cognitive Linguistics**, Концепт, Фрейм, Манзара | `knowledge_base/06_uzbek_linguistics_and_pragmatics/` | Safarov (2006) (`Kognitiv tilshunoslik...md`) |
| **Uzbek Media Text Perception**, Газета матнлари перцепцияси | `knowledge_base/06_uzbek_linguistics_and_pragmatics/` | Azimova (2008) (`И_А_Азимova...md`) |
| **Uzbek Bilingualism / Child Language Ontogenesis** | `knowledge_base/06_uzbek_linguistics_and_pragmatics/` | Shamsieva (2019) (`22.md`) |
| **Uzbek Literary Analysis & Lingvopoetics** | `knowledge_base/06_uzbek_linguistics_and_pragmatics/` | Abuzalova (2024), Xudoyberganova (2022), Musulmanova (2023) |

---

## 3. Querying & Search Automation

To retrieve exact paragraphs, definitions, or citations programmatically, use `search_kb.py`:

```bash
# General search
python search_kb.py "propositional network"

# Search in a specific subcategory
python search_kb.py "интерфейсная теория" --category 01

# Filter by language ('en', 'ru', 'uz')
python search_kb.py "концепт" --lang uz

# Expand surrounding context lines
python search_kb.py "event indexing" --context 4 --limit 3

# Browse all indexed academic themes
python search_kb.py --topics

# Full catalog summary
python search_kb.py --summary
```

---

## 4. Cross-Linguistic Terminology Reference

When users ask questions across languages, use these equivalents to find the right sections in Russian, English, or Uzbek:

| English Concept | Russian Equivalent | Uzbek Equivalent |
| :--- | :--- | :--- |
| Speech Production | Порождение речи | Нутқ ҳосил бўлиши / нутқ генерацияси |
| Speech Perception / Comprehension | Восприятие / понимание речи | Нутқни идрок этиш / тушуниш |
| Mental Lexicon | Внутренний менталный лексикон | Ментал лексикон / ички луғат |
| Situation Model | Ситуационная модель | Вазият (ситуатив) модели |
| Textbase / Proposition | Пропозициональная база текста | Пропозиционал структура / матн базаси |
| Discourse Comprehension | Понимание дискурса | Дискурсни тушуниш |
| Embodied Cognition | Воплощенное познание / симуляция | Гавдаланган когниция / ментал симуляция |
| Narrative Transportation | Нарративная транспортировка | Нарратив трансформация / матнга сингиш |
| Emotional Dominant | Эмоционально-смысловая доминанта | Эмоционал-мазмуний доминанта |
| Speech Act Theory | Теория речевых актов | Нутқ актлари назарияси |
| Presupposition | Пресуппозиция | Пресуппозиция |
| Bilingualism | Билингвизм / двуязычие | Билингвизм / икки тиллилик |

---

## 5. Academic Citation Guidelines for AI

When generating syntheses, research notes, or answers for the user:
1. Always cite author, year, and work title (e.g. `(Levelt, 1989, Chapter 4)` or `(Сафаров, 2008, 2-боб)`).
2. Reference the exact relative path in `knowledge_base/...` so the user can inspect the primary text.
3. If quoting directly, quote accurately from the Markdown file and mention the page comment marker (`<!-- Page N -->` / `<!-- Стр. N -->` / `<!-- Бет N -->`).

