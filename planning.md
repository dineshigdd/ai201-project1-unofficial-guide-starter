# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Student reviews and survival guides for Computer Science professors and classes at Cal Poly Pomona.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size: 300**

**Overlap: 30**

**Reasoning: I choose recursive strategy because my review can contain about 1 to 3 sentences.This strategy will not cut mid-word or mid-thoought**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** `all-MiniLM-L6-v2`

**Top-k:** 4

**Production tradeoff reflection:**
I would choose a moldel with a higher context length, accuracy , and domain-specifice text. A premium model would understand student slang better and make fewer mistakes finding files, even though its massive capacity is a bit of an overkill for my short reviews.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is considered the hardest core Computer Science course to pass at Cal Poly Pomona ? | CS 4310, CS 3310, CS 3110, CS 4310, CS 3650 |
| 2 | Which Computer Science professors do students recommend avoiding at Cal Poly  Pomona  ?  | Nima Davarpanah,Sallam Salloum, Nhi Nguyen ,Peter Laszlo |
| 3 | Who are considered the best Computer Science professors at Cal Poly Pomona to take algorithm and data structures ? | Crisrael Lucero,Markus Eger ,Yu Sun , Edwin Rodriguez|
| 4 | What is the best place to study on campus at Cal Poly Pomona according to students? | The University Library 6th Floor, Student Services Building Center Courtyard, The Cave (Building 97)|
| 5 | What are the best three off-campus dining places near Cal Poly Pomona based on top student reviews? | Koji Ramen, Pho 909, Sugar Rush Cafe |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Incomplete sentences and complicated punctuation could result in challenges when separating chunks, which could lead to sentences being cut mid-thought and missing critical information

2. Reviews and comments are not always focused on a single topic. For example, a student might ask a question about a specific class, but the replies often include details that are completely irrelevant to the original post. Reddit threads are highly informal; students frequently drift into discussions about unrelated classes, different professors, other universities, or even personal experiences that have nothing to do with the question raised. This makes preparing the documents much more challenging, as these off-topic comments can introduce noise into the database and mislead the model during retrieval.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

![RAG Pipeline Architecture](./images/unofficial-guide-arch.png)
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
- **AI Tools:** Claude Code, Gemini (to prepare documents)
- **Input:** `planning.md` and other necessary inputs based on project requirements
- **Output:** `ingest.py`, which contains the code that transforms text files in the `documents` folder into highly organized chunks
- **Verification:** Reviewed and tested the generated code, using `planning.md` as a guideline to check if the AI produced the intended output

**Milestone 4 — Embedding and retrieval:**
- **AI Tools:** `all-MiniLM-L6-v2` via `sentence-transformers`, Claude Code
- **Input:** Chunks produced from Milestone 3, `planning.md`, and the project architecture guidelines
- **Output:** `embed.py`, a script designed to load an embedding model, initialize a local vector database, and provide a basic mechanism to query and retrieve relevant text snippets
- **Verification:** Run a test query—for example, "What is the best place to study on campus at Cal Poly Pomona according to students?"—and check the top-k retrieved chunks from ChromaDB against anticipated answers to ensure the vector store successfully isolates the most semantically relevant information before passing it to an LLM in the next stage

**Milestone 5 — Generation and interface:**
- **AI Tools:** Claude Code (for development) and Groq API
- **Input:** User query, the top-k text chunks retrieved from `embed.py`, and a structured system prompt
- **Output:** `app.py`, which handles the Groq API client connection, provides an interactive UI, and lists the sources used
- **Verification:** Run the evaluation questions through the full pipeline to verify that Groq synthesizes the retrieved chunks into fast, natural, and accurately grounded student answers while maintaining low latency
