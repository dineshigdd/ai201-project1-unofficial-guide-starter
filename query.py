"""
query.py — Milestone 5: Grounded Generation (pipeline logic)
=============================================================

Final stage of the RAG pipeline (see images/unofficial-guide-arch.png):

    Ingestion -> Chunking -> Embedding + Vector Store -> Retrieval -> [Generation]
                                                                       ^^^^^^^^^^^^

Takes a user question, retrieves the top-k chunks (via embed.retrieve), and asks
the Groq-hosted LLM to answer **using only those chunks**. Returns a structured
result containing the answer plus a programmatically-captured list of sources —
source attribution does not depend on the model formatting citations itself.

Run `python query.py "your question"` for a quick CLI test.
"""

from __future__ import annotations

import os
import sys

from dotenv import load_dotenv
from groq import Groq

from embed import retrieve, TOP_K

# --- Configuration -----------------------------------------------------------
load_dotenv()  # reads GROQ_API_KEY from .env (python-dotenv, per the diagram)

LLM_MODEL = "llama-3.3-70b-versatile"   # default Groq engine
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

_client: Groq | None = None


def get_client() -> Groq:
    """Create (once) the Groq client, loading the key securely from .env."""
    global _client
    if _client is None:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key or api_key == "your_key_here":
            raise RuntimeError(
                "GROQ_API_KEY is missing. Copy .env.example to .env and add your "
                "key from https://console.groq.com"
            )
        _client = Groq(api_key=api_key)
    return _client


def build_prompt(query: str, chunks: list[dict]) -> str:
    """Assemble the user-turn prompt: numbered context blocks + the question."""
    context_blocks = []
    for i, c in enumerate(chunks, 1):
        context_blocks.append(
            f"[{i}] (source: {c['source']}, subject: {c['subject']})\n{c['text']}"
        )
    context = "\n\n".join(context_blocks) if context_blocks else "(no documents)"
    return (
        f"CONTEXT:\n{context}\n\n"
        f"QUESTION: {query}\n\n"
        "Answer using only the context above."
    )


def answer_question(query: str, k: int = TOP_K) -> dict:
    """Run the full retrieve -> generate pipeline.

    Returns a structured dict:
        {
          "answer":  str,            # grounded generated text
          "sources": list[str],      # unique source files used, e.g. "best-places.txt"
          "chunks":  list[dict],     # the raw retrieved chunks (for inspection)
        }
    Source attribution is captured programmatically from retrieval — it never
    depends on the model formatting citations.
    """
    chunks = retrieve(query, k=k)

    # Programmatic source attribution: unique files, order preserved by rank.
    sources: list[str] = []
    for c in chunks:
        if c["source"] not in sources:
            sources.append(c["source"])

    if not chunks:
        return {"answer": FALLBACK, "sources": [], "chunks": []}

    completion = get_client().chat.completions.create(
        model=LLM_MODEL,
        temperature=0.2,          # low temperature keeps answers grounded
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(query, chunks)},
        ],
    )
    answer = completion.choices[0].message.content.strip()

    return {"answer": answer, "sources": sources, "chunks": chunks}


def main() -> None:
    query = " ".join(sys.argv[1:]) or "What do students say about Fuh Sang?"
    print(f"Q: {query}\n")
    result = answer_question(query)
    print(f"A: {result['answer']}\n")
    print("Retrieved from:")
    for s in result["sources"]:
        print(f"  • {s}")


if __name__ == "__main__":
    main()
