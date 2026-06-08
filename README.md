# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
The topic I chose is `Student reviews and survival guides for Computer Science professors and classes at Cal Poly Pomona.`

The reason why I decided to choose this topic is because only past students can share the real experience with prospective students. While students can read about professors on the campus website or LinkedIn, I believe, based on my past experience, that student reviews are very useful for finding a professor who can effectively teach the subject. Student reviews provide a good overall picture of professors' teaching styles, expectations for students, and how challenging a particular course could be.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Reddit (ACC 3110) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/nslt98/acc_3110/ |
| 2 | RateMyProfessors (ID: 2687117) | Professor Review | https://www.ratemyprofessors.com/professor/2687117 |
| 3 | Reddit (Fuh Sang vs Dominick Atanasio) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/7z786g/cs_professor_fuh_sang_or_dominick_atanasio/ |
| 4 | Reddit (CS 3310 w/ Salloum) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/9r1haq/cs_3310_w_salloum/ |
| 5 | RateMyProfessors (ID: 2372423) | Professor Review | https://www.ratemyprofessors.com/professor/2372423 |
| 6 | RateMyProfessors (ID: 2647317) | Professor Review | https://www.ratemyprofessors.com/professor/2647317 |
| 7 | RateMyProfessors (ID: 2525429) | Professor Review | https://www.ratemyprofessors.com/professor/2525429 |
| 8 | RateMyProfessors (ID: 1548624) | Professor Review | https://www.ratemyprofessors.com/professor/1548624 |
| 9 | RateMyProfessors (ID: 2843849) | Professor Review | https://www.ratemyprofessors.com/professor/2843849 |
| 10 | RateMyProfessors (ID: 2517026) | Professor Review | https://www.ratemyprofessors.com/professor/2517026 |
| 11 | RateMyProfessors (ID: 126937) | Professor Review | https://www.ratemyprofessors.com/professor/126937 |
| 12 | RateMyProfessors (ID: 2322230) | Professor Review | https://www.ratemyprofessors.com/professor/2322230 |
| 13 | Reddit (Best/Underrated Study Places) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/tnoob3/bestunderrated_place_to_study_at/ |
| 14 | RateMyProfessors (ID: 1822204) | Professor Review | https://www.ratemyprofessors.com/professor/1822204 |
| 15 | Reddit (College Orientation) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/12wmfuj/college_orientation/ |
| 16 | Reddit (CS 2560 w/ Nguyen) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/98faud/cs2560_c_programming_w_nguyen_should_i_drop/ |
| 17 | Reddit (CS Undergraduate Seminar) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/i7a7aa/cs_undergraduate_seminar_class/ |
| 18 | RateMyProfessors (ID: 1030761) | Professor Review | https://www.ratemyprofessors.com/professor/1030761 |
| 19 | Reddit (CS Advice: Damavandi vs Sang) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/bzvxz2/cs_advice_for_fall_damavandi_vs_sang/ |
| 20 | RateMyProfessors (ID: 901042) | Professor Review | https://www.ratemyprofessors.com/professor/901042 |
| 21 | Uloop (Fang Tang) | Professor Review | https://csupomona.uloop.com/professors/view.php/897658/Fang-Tang |
| 22 | Uloop (David Dear) | Professor Review | https://csupomona.uloop.com/professors/view.php/41864/David-Dear |
| 23 | Uloop (Craig Rich) | Professor Review | https://csupomona.uloop.com/professors/view.php/42420/Craig-Rich |
| 24 | Reddit (Fun Places to Eat/See Near CPP) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/1jrzs8b/fun_place_to_eat_and_things_to_see_near_cpp/ |
| 25 | Reddit (Popular Eateries Near Campus) | Discussion Thread | https://www.reddit.com/r/CalPolyPomona/comments/1dmeekw/popular_eateries_places_to_go_onnear_campus/ |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
- 300
**Overlap:**
- 30 
**Why these choices fit your documents:**
I choose `recursive strategy` because my review can contain about 3 or more sentences. I wanted a chunking strategy that would not cut mid-word or mid-thoughts in the documents.

In preparing the documents before chunking , I try to keep a similar structure in every document. I minimize the use of heading so that the documents will be simple to process.

**Final chunk count:**
| Document | Chunks |
| :--- | :--- |
| best-places.txt | 19 |
| best-professors.txt | 38 |
| CS2600.txt | 30 |
| CS3110.txt | 19 |
| CS3310.txt | 20 |
| CS3650.txt | 25 |
| CS4310.txt | 9 |
| general-advice.txt | 12 |
| off-campus-dinning.txt | 39 |
| tough-professors.txt | 42 |
| **Total** | **253** |
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
