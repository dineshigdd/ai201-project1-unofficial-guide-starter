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

**Model used:** `all-MiniLM-L6-v2`

**Production tradeoff reflection:**  

I would choose a model with a higher context length, high accuracy, and strong performance on domain-specific text. Context length is critical because it allows the model to analyze and extract details from a larger number of student reviews, providing the bigger picture to the user. Models with high accuracy can understand and capture the meaning of two or more sentences written with a different choice of words, understand the distinct context when the same words are used, and provide superior dimensional granularity (the level of detail and nuance the AI can see when it reads a sentence). Because students can use a mix of formal, informal, and slang language, handling domain-specific text is also a critical aspect.  
Thus, I would choose a premium model that will make fewer mistakes when finding files, even though its massive capacity is a bit of overkill for my short reviews.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
The system prompt contains the following rules:

1. Answer strictly from the CONTEXT — do not use outside or prior knowledge.
2. If the context lacks enough information, reply with the exact fallback string "I don't have enough information on that."
3. Do not invent professors, courses, places, or facts not present in the context.
4. Be concise and base every claim on the provided reviews.

The prompt is implemented in `query.py`:

```python
FALLBACK = "I don't have enough information on that."

SYSTEM_PROMPT = (
    "You are The Unofficial Guide, a helpful assistant that answers questions "
    "about Cal Poly Pomona using ONLY student reviews provided to you.\n"
    "Rules:\n"
    "1. Answer strictly from the CONTEXT below. Do NOT use any outside or prior "
    "knowledge.\n"
    "2. If the context does not contain enough information to answer the "
    f"question, reply with exactly: \"{FALLBACK}\"\n"
    "3. Do not invent professors, courses, places, or facts that are not in the "
    "context.\n"
    "4. Be concise and base every claim on the provided reviews."
)

```
There are two structural choices:

`Context formatting` — the top-4 retrieved chunks are injected as numbered blocks, each tagged with its source file and subject, so the model sees clearly delimited evidence rather than a blurred wall of text.

`Low-Temperature Configuration:` — I explicitly configured the Groq engine with a low temperature of 0.2. This configuration reduces creative drift, limits the model’s randomness ,and keep the output close to the supplied reviews.


**How source attribution is surfaced in the response:**  
Sources are stored in a list and ordered by rank. These sources are displayed separately in a textbox within the frontend UI.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What is considered the hardest core Computer Science course to pass at Cal Poly Pomona ? | CS 4310, CS 3110, CS3310, CS 4310, CS 3650 | CS 3110 "one of the most challenging"| Partially relevant | partially accurate |
| 2 | Which Computer Science professors do students recommend avoiding at Cal Poly Pomona  ?  | Nima Davarpanah,Sallam Salloum, Nhi Nguyen ,Peter Laszlo | Tony Diaz, Edwin Rodriguez, Dominick Atanasio, Saleem Saleem, Sandler, Thomas Huang, Thanh Nguyen |Partially relevant |  Partially accurate |
| 3 | Who are considered the best Computer Science professors at Cal Poly Pomona to take algorithm and data structures ? | Crisrael Lucero,Markus Eger ,Yu Sun , Edwin Rodriguez| David Johansson, Yu Sun, Navi, Eger, and Professor Fuh Sang(and provides more information )| | Partially relevant || Partially accurate |
| 4 | What is the best place to study on campus at Cal Poly Pomona according to students? | The University Library 6th Floor, Student Services Building Center Courtyard, The Cave (Building 97)|I don't have enough information on that| Off-target | Accurate |
| 5 | What are the best three off-campus dining places near Cal Poly Pomona based on top student reviews? | Koji Ramen, Pho 909, Sugar Rush Cafe | Cal Poly Pomona Farm Store (across the street), Nambah Cafe (a little further up near La Verne, basically right across the university)| Off-target  |Inaccurate |


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
`What are the best three off-campus dining places near Cal Poly Pomona based on top student reviews?`
**What the system returned:**
`
Based on the context, the following are mentioned as off-campus dining places near Cal Poly Pomona: 
1. Cal Poly Pomona Farm Store (across the street)
2. Nambah Cafe (a little further up near La Verne, basically right across the university)

Starbucks is mentioned, but it's on campus, not off-campus. The Campus Quad is also mentioned, but it's not a dining place. 

Since there are only two off-campus dining places mentioned, I don't have enough information on the third one.
`
**Root cause (tied to a specific pipeline stage):**
The model retrieved chunks from best-places.txt and off-campus-dining.txt. However, these specific documents lacked the necessary context or factual evidence required to rank the 'best three' places. Ideally, the LLM should have strictly adhered to its system instructions and responded with: 'I don't have enough information on that.

The root cause of the issue is a limitation in the text-transformation step. Because the model used to read and process the text has a strict limit on how much text it can look at at one time, it cannot grasp the full idea if the text is too long. If the important dining reviews were placed too far down in the document, they were cut off before being saved. Because the system missed this information, it couldn't understand it and ended up pulling the wrong files.
 
**What you would change to fix it:**
The best way to fix this, within our technical constraints, is to add more information to off-campus-dining.txt and shorten the sentence length. Breaking the reviews into shorter, smaller pieces ensures that the text stays under the limit and does not get cut off, allowing the model to fully grasp the information.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec helped me to understand what the system does and how the system functions in detail. I learned the architecture of a RAG system and the steps to build it. Additionally, completing the spec provided me an opportunity to explore the technologies behind these RAG systems, their limitations, and other premium models that I could use in a production environment.

**One way your implementation diverged from the spec, and why:**
My planning.md specified a 300-character chunk size, but my actual chunks reach up to 341 characters. The difference comes from a design decision during the implementation. Each review is splited to 300 characters first, then  the review's subject is added (like the professor, place, or course name) to the front of every chunk.

The review text itself still respects the 300-character limit, but the subject prefix pushes the final chunk size slightly over. I accepted this because it directly solves Anticipated Challenge #1. When splitting a long review, a fragment like 'frequently for personal issues' is completely meaningless without knowing it refers to Professor David Gershman. Adding those extra characters preserves the subject connection that strict 300-character chunking would have cut off, which I judged to be more important than holding exactly to the limit

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
     I provided code claude with architecture of the system and ask to implement the ingest.py. I prompted to use planning.md to implement the ingestion phase,and include the code in ingest.py. Claude produce the following code ( only the functin signature are listed here). 

- *What it produced:*  

          | Function Signature | Description |
          |---|---|
          | `recursive_split(text: str, separators: list[str]) -> list[str]` | Handles dividing the text into smaller pieces based on natural boundaries without crossing the maximum character limit. |
          | `_apply_overlap(chunks: list[str]) -> list[str]` | A helper function that attaches text from the tail end of a previous chunk to the next chunk to handle the 30-character overlap strategy. |
          | `parse_reviews(raw: str) -> list[tuple[str, str]]` | Steps through raw document lines to extract headers (like professor names or locations) and match them up with their specific reviews. |
          | `flush()` (Nested Function) | A local helper function defined inside `parse_reviews` used to bundle and clean up text segments before saving them to the main tracking list. |
          | `chunk_document(path: Path) -> list[Chunk]` | Coordinates reading an individual text file, sending it through the parser, breaking it up, and mapping everything to Chunk data objects. |
          | `ingest(documents_dir: Path = DOCUMENTS_DIR) -> list[Chunk]` | Loops through your entire directory of .txt files to run the chunking process across all files in a batch. |



- *What I changed or overrode:*  
     In planning.md, the maximum chunk size is defined as 300 characters. While this is sufficient to hold the actual review text, additional details are added to each chunk to make it more meaningful. After testing and reviewing the code, I decided to keep this implementation because I found it is best to preserve that extra context, even though it means the final chunk size is dynamically modified.

**Instance 2**

- *What I gave the AI:*  
     I used AI to help prepare the documentation used by ingest.py. First, I used a tool like `Reddinbox` to convert Reddit comments into text. Then, I took this raw text and prompted the AI (Gemini) to organize it into a specific structure I provided. For comments on JavaScript-heavy websites where scraping was difficult, I manually copied and pasted the text and then used the AI to organize it into my required structure.

- *What it produced:*  
     The AI produced cleanly organized text that followed the exact structure I provided.

- *What I changed or overrode:*  
     I changed some of the punctuation, fixed incomplete sentences, and adjusted a few headings. When making these changes, I was very careful not to alter the original meaning of the reviews. Ultimately, the adjustments I had to make were minor.
