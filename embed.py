"""
embed.py — Milestone 4: Embedding + Vector Store + Retrieval
=============================================================

Stages 3-5 of the RAG pipeline (see images/unofficial-guide-arch.png):

    Ingestion -> Chunking -> [Embedding + Vector Store] -> [Retrieval] -> Generation
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^    ^^^^^^^^^^^

This module:
  3. Embedding    — encodes each chunk with sentence-transformers
                    `all-MiniLM-L6-v2` into 384-dimensional vectors.
  4. Vector Store — persists those vectors in a local ChromaDB collection
                    configured for cosine similarity.
  5. Retrieval    — embeds a user query and returns the top-k (=4) most
                    similar chunks via ChromaDB's cosine search.

Run `python embed.py` to (re)build the index from chunks.json, then a smoke-test
query is run automatically. Milestone 5 (generation) will import `retrieve()`.
"""

from __future__ import annotations

import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

# --- Configuration (matches the Retrieval Approach section of planning.md) ---
BASE_DIR = Path(__file__).parent
CHUNKS_FILE = BASE_DIR / "chunks.json"
CHROMA_DIR = BASE_DIR / "chroma_db"          # local persistent storage
COLLECTION_NAME = "unofficial_guide"

EMBED_MODEL = "all-MiniLM-L6-v2"             # 384-dim, from the diagram
TOP_K = 4                                    # chunks retrieved per query

# Cache the model so we load the weights only once per process.
_model: SentenceTransformer | None = None


def get_model() -> SentenceTransformer:
    """Load (once) and return the sentence-transformers embedding model."""
    global _model
    if _model is None:
        print(f"Loading embedding model: {EMBED_MODEL}")
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Encode a list of texts into normalized 384-dim vectors.

    Vectors are L2-normalized so ChromaDB's cosine distance behaves as a clean
    1 - cosine_similarity score.
    """
    embeddings = get_model().encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=len(texts) > 50,
    )
    return embeddings.tolist()


def get_client() -> chromadb.ClientAPI:
    """Return a ChromaDB client backed by local on-disk storage."""
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def get_collection(create: bool = False) -> chromadb.Collection:
    """Get the guide's collection, configured for cosine similarity."""
    client = get_client()
    if create:
        return client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
    return client.get_collection(name=COLLECTION_NAME)


def build_index() -> int:
    """Load chunks.json, embed every chunk, and (re)store them in ChromaDB.

    Returns the number of chunks indexed.
    """
    if not CHUNKS_FILE.exists():
        raise FileNotFoundError(
            f"{CHUNKS_FILE.name} not found — run `python ingest.py` first."
        )

    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    print(f"Loaded {len(chunks)} chunks from {CHUNKS_FILE.name}")

    # Start clean so re-running never duplicates or leaves stale vectors.
    client = get_client()
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass  # collection didn't exist yet
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    ids = [c["id"] for c in chunks]
    documents = [c["text"] for c in chunks]
    metadatas = [
        {"source": c["source"], "subject": c["subject"],
         "chunk_index": c["chunk_index"]}
        for c in chunks
    ]

    print("Embedding chunks...")
    embeddings = embed_texts(documents)

    # Add in batches to stay well under ChromaDB's per-call limits.
    batch = 128
    for i in range(0, len(ids), batch):
        sl = slice(i, i + batch)
        collection.add(
            ids=ids[sl],
            documents=documents[sl],
            metadatas=metadatas[sl],
            embeddings=embeddings[sl],
        )

    print(f"Indexed {collection.count()} chunks into '{COLLECTION_NAME}' "
          f"at {CHROMA_DIR.name}/")
    return collection.count()


def retrieve(query: str, k: int = TOP_K) -> list[dict]:
    """Return the top-k chunks most similar to `query`.

    Each result dict has: text, source, subject, chunk_index, score
    (score = cosine similarity in [0, 1], higher is more relevant).
    """
    collection = get_collection()
    query_embedding = embed_texts([query])[0]

    res = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    results: list[dict] = []
    for doc, meta, dist in zip(
        res["documents"][0], res["metadatas"][0], res["distances"][0]
    ):
        results.append({
            "text": doc,
            "source": meta["source"],
            "subject": meta["subject"],
            "chunk_index": meta["chunk_index"],
            "score": round(1 - dist, 4),  # cosine distance -> similarity
        })
    return results


def main() -> None:
    build_index()

    # Smoke test: one of the evaluation questions from planning.md.
    question = "What is the best place to study on campus?"
    print(f"\nSmoke-test query: {question!r}\n")
    for i, r in enumerate(retrieve(question), 1):
        print(f"[{i}] score={r['score']:.3f}  source={r['source']}  "
              f"subject={r['subject']}")
        print(f"    {r['text'][:120]}...\n")


if __name__ == "__main__":
    main()
