"""
ingest.py — Milestone 3: Document Ingestion + Chunking
=======================================================

First stage of the RAG pipeline described in planning.md:

    Ingestion -> Chunking -> Embedding + Vector Store -> Retrieval -> Generation
    ^^^^^^^^^^^^^^^^^^^^^^

This module reads the plain-text student reviews in ./documents and turns them
into overlapping text chunks ready for embedding in Milestone 4.

Chunking strategy (from planning.md):
    - Chunk size : 300 characters
    - Overlap    : 30 characters
    - Recursive  : split on the largest natural boundary that fits, so we never
                   cut a chunk mid-word or mid-thought. Reviews are short
                   (1-3 sentences), so most reviews become a single chunk.

Each document is review-based with a header naming the subject
(`Professor:`, `Name:`, `Location:`, `Course ID:`) and individual reviews
separated by a line containing only `---`. We carry that subject forward as
metadata on every chunk, so a chunk still "knows" which professor / place /
course it is about even when a long review is split across boundaries.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path

# --- Configuration (matches the Chunking Strategy section of planning.md) ----
DOCUMENTS_DIR = Path(__file__).parent / "documents"
OUTPUT_FILE = Path(__file__).parent / "chunks.json"

CHUNK_SIZE = 300       # max characters per chunk
CHUNK_OVERLAP = 30     # characters shared between adjacent chunks

# Header labels that announce the subject of the reviews that follow.
SUBJECT_LABELS = ("Course ID:", "Professor:", "Name:", "Location:")

# Separators tried in order, largest natural boundary first. The final ""
# guarantees forward progress even if a single "word" is longer than CHUNK_SIZE.
SEPARATORS = ["\n\n", "\n", ". ", " ", ""]


@dataclass
class Chunk:
    """One retrievable unit of text plus the metadata we attach for grounding."""
    id: str             # stable id, e.g. "CS3110.txt::3"
    text: str           # the chunk content (subject prefix + review text)
    source: str         # originating filename, e.g. "CS3110.txt"
    subject: str        # professor / place / course this chunk is about
    chunk_index: int    # position of this chunk within its source document


def recursive_split(text: str, separators: list[str]) -> list[str]:
    """Split `text` into <= CHUNK_SIZE pieces, preferring large separators.

    Mirrors the idea behind LangChain's RecursiveCharacterTextSplitter without
    the dependency: try to break on paragraphs, then lines, then sentences,
    then words, falling back to a hard character cut only as a last resort.
    """
    text = text.strip()
    if len(text) <= CHUNK_SIZE:
        return [text] if text else []

    separator = separators[-1]
    remaining = separators[:]
    for i, sep in enumerate(separators):
        if sep == "" or sep in text:
            separator = sep
            remaining = separators[i + 1:]
            break

    # Break into the smallest splits this separator produces...
    if separator == "":
        pieces = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    else:
        pieces = [p for p in text.split(separator) if p != ""]

    # ...then greedily merge them back up to CHUNK_SIZE, recursing on any
    # single piece that is still too large for the current separator.
    chunks: list[str] = []
    buffer = ""
    join = separator if separator != "" else ""
    for piece in pieces:
        if len(piece) > CHUNK_SIZE:
            if buffer:
                chunks.append(buffer.strip())
                buffer = ""
            chunks.extend(recursive_split(piece, remaining))
            continue

        candidate = piece if not buffer else buffer + join + piece
        if len(candidate) <= CHUNK_SIZE:
            buffer = candidate
        else:
            chunks.append(buffer.strip())
            buffer = piece
    if buffer.strip():
        chunks.append(buffer.strip())

    return [c for c in chunks if c]


def _apply_overlap(chunks: list[str]) -> list[str]:
    """Prepend the tail of the previous chunk to each chunk for CHUNK_OVERLAP."""
    if CHUNK_OVERLAP <= 0 or len(chunks) <= 1:
        return chunks
    out = [chunks[0]]
    for prev, cur in zip(chunks, chunks[1:]):
        tail = prev[-CHUNK_OVERLAP:].lstrip()
        out.append(f"{tail} {cur}".strip())
    return out


def parse_reviews(raw: str) -> list[tuple[str, str]]:
    """Walk a document line by line, yielding (subject, review_text) pairs.

    Tracks the most recent subject header and splits the review body on lines
    that contain only `---`.
    """
    subject = "Unknown"
    pairs: list[tuple[str, str]] = []
    current: list[str] = []

    def flush():
        body = "\n".join(current).strip()
        if body:
            pairs.append((subject, body))
        current.clear()

    for line in raw.splitlines():
        stripped = line.strip()
        matched_label = next(
            (lbl for lbl in SUBJECT_LABELS if stripped.startswith(lbl)), None
        )
        if matched_label:
            flush()
            subject = stripped[len(matched_label):].strip() or subject
        elif stripped == "Reviews:":
            continue  # structural header, carries no review text
        elif stripped == "---":
            flush()
        else:
            current.append(line)
    flush()
    return pairs


def chunk_document(path: Path) -> list[Chunk]:
    """Read one .txt file and return its list of Chunk objects."""
    raw = path.read_text(encoding="utf-8")
    chunks: list[Chunk] = []
    index = 0

    for subject, review in parse_reviews(raw):
        # Prefix the subject so a split review still names what it's about.
        prefix = f"{subject}: " if subject and subject != "Unknown" else ""
        for piece in _apply_overlap(recursive_split(review, SEPARATORS)):
            text = f"{prefix}{piece}".strip()
            chunks.append(
                Chunk(
                    id=f"{path.name}::{index}",
                    text=text,
                    source=path.name,
                    subject=subject,
                    chunk_index=index,
                )
            )
            index += 1

    return chunks


def ingest(documents_dir: Path = DOCUMENTS_DIR) -> list[Chunk]:
    """Ingest and chunk every .txt file in `documents_dir`."""
    files = sorted(documents_dir.glob("*.txt"))
    if not files:
        raise FileNotFoundError(f"No .txt files found in {documents_dir}")

    all_chunks: list[Chunk] = []
    for path in files:
        doc_chunks = chunk_document(path)
        all_chunks.extend(doc_chunks)
        print(f"  {path.name:<24} -> {len(doc_chunks):>3} chunks")
    return all_chunks


def main() -> None:
    print(f"Ingesting documents from {DOCUMENTS_DIR}\n")
    chunks = ingest()

    OUTPUT_FILE.write_text(
        json.dumps([asdict(c) for c in chunks], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lengths = [len(c.text) for c in chunks]
    print(f"\nDone. {len(chunks)} chunks from "
          f"{len(set(c.source for c in chunks))} documents.")
    print(f"  chunk length: min {min(lengths)}, "
          f"max {max(lengths)}, avg {sum(lengths) // len(lengths)} chars")
    print(f"  written to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
