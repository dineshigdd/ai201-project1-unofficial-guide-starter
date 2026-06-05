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

<!-- | # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | rate my professors | Standardized metrics and student feedback strings for CPP faculty. | https://www.ratemyprofessors.com/school/153 |
| 2 | reddit | The central hub for student debates, course planning, and syllabus reviews. | https://www.reddit.com/r/CalPolyPomona/ |
| 3 | the poly post | CPP's student-run newspaper featuring editorials on registration and academic policies. | https://thepolypost.com/ |
| 4 | cpp uloop | Campus marketplace featuring standalone professor evaluations and student grading metrics. | https://cpp.uloop.com/professors/ |
| 5 | niche | Long-form student surveys and essay reviews detailing workload management at CPP. | https://www.niche.com/colleges/california-state-polytechnic-university-pomona/ |
| 6 | gradreports | High-quality text reviews from recent CPP alumni breaking down major departments. | https://www.gradreports.com/colleges/california-state-polytechnic-university-pomona |
| 7 | appily | Localized student journals detailing specific quarter/semester course experiences. | https://www.appily.com/colleges/california-state-polytechnic-university-pomona/reviews |
| 8 | unigo | Paragraph-length student responses detailing academic stress and instructor quality. | https://www.unigo.com/colleges/california-state-polytechnic-university-pomona |
| 9 | college confidential | Student forum threads analyzing academic workloads, gatekeeper classes, and faculty reputations | https://talk.collegeconfidential.com/t/deciding-between-cpp-and/1972220 |
| 10 | Quora | Text reviews from CPP instructional student assistants and tutors detailing department environments. | https://www.quora.com/How-good-is-computer-science-undergrad-program-at-cal-poly-Pomona |
|11 | collegevine | Text review |https://www.collegevine.com/faq/20309/uc-riverside-vs-cal-poly-pomona-which-one-for-computer-science|
| 12 | https://talk.collegeconfidential.com/t/does-cal-poly-pomona-have-a-good-cs-program/2043520/9 -->
| # | Source | Description | URL or location |
| :--- | :--- | :--- | :--- |
| 1 | coursicle | search tool and reviews on courses and professors |https://www.coursicle.com/calpoly/courses/CSC/|
| 2 | Reddit Thread | most distinguished Computer Science teachers on campus |https://www.reddit.com/r/CalPolyPomona/comments/5epd25/who_are_the_most_distinguished_computer_science/ |
| 3 | Rate My Professors | reviews about the college. | https://www.ratemyprofessors.com/school/13914 |
| 4 | Rate My Professors | Student evaluation history tracking foundational programming sequences under Bahram Zartoshty. | https://www.ratemyprofessors.com/professor/1908332 |
| 5 | Rate My Professors | Academic difficulty reviews and project expectations for computer architecture under Dr. Robert Mcllhenny. | https://www.ratemyprofessors.com/professor/140733 |
| 6 | Reddit Thread | Community student consensus ranking the absolute hardest upper-division gatekeeper CS courses. | https://www.reddit.com/r/CalPolyPomona/comments/11v36df/hardest_cs_classes_at_cpp/ |
| 7 | Reddit Thread | Upperclassmen study blueprints and execution tips for passing Assembly Language coding tracks. | https://www.reddit.com/r/CalPolyPomona/comments/9z818b/how_is_cs_2640_with_assembly/ |
| 8 | College Confidential | Educational board discussions weighing CPP's technical curriculum against other regional engineering universities. | https://talk.collegeconfidential.com/t/deciding-between-cpp-and/1972220 |
| 9 | GradReports | Post-graduation alumni essays evaluating how effectively the "Learn by Doing" CS curriculum prepared them for software engineering jobs. | https://www.gradreports.com/colleges/california-state-polytechnic-university-pomona |
| 10 | CPP CSS Homepage | Unofficial hub tracking student-run software projects, technical frameworks, and extracurricular coding workshops. | https://cpp-css.github.io/ |

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
| 1 | What is the hardest core Computer Science courses to pass at cal poly pomona | CS 3110 |
| 2 | Who is the computer science professors to avoid at cal poly pomona  | Nima Davarpanah,Sallam Salloum, Nhi Nguyen ,Peter Laszlo |
| 3 | Who are the best and easiest computer science professors in cal poly pomona | Crisrael Lucero,Markus Eger ,Yu Sun , Edwin Rodriguez|
| 4 | What is the best place to study on campus in cal ploy pomona | The Library Quiet Zones (Floors 1, 5, and 6)|
| 5 | What is the best time to apply for cal poly pomona | priority filing period from  October 1 to November 30 |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Incomplte reviews , chunks that would cut off critical information

2. Too many slang , ironic use of words, 

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

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
