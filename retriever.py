import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS

# Embedding function and ChromaDB client are initialized once at module load.
# sentence-transformers downloads the model on first use — this may take
# 30–60 seconds the very first time. Subsequent runs use a local cache.
_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    """Return the ChromaDB collection. Used during ingestion."""
    return _collection


def embed_and_store(chunks):
    """
    Embed a list of chunks and store them in the vector database.

    _collection.add() takes three parallel lists built from the chunks
    returned by chunk_document():
      - documents : raw text strings — ChromaDB's embedding function converts
                    these to vectors automatically using sentence-transformers
      - metadatas : one dict per chunk, storing source_name and url so that
                    retrieve() can surface where a result came from
      - ids       : the unique chunk_id strings used to identify each entry
    """
    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source_name": c["source_name"], "url": c["url"]} for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print(f"Stored {_collection.count()} total chunks in the vector database.")


def retrieve(query, n_results=N_RESULTS):
    """
    Find the most relevant restaurant chunks for a user's question.

    Uses _collection.query() to run a semantic search. Returns a list of
    dicts, each with:
      - "text"        : the chunk text
      - "source_name" : the source the chunk came from (e.g. "Eating The Ave")
      - "url"         : the source URL
      - "distance"    : the similarity score (lower = more similar for cosine)
    """
    if _collection.count() == 0:
        return []

    results = _collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    chunks = [
        {
            "text": text,
            "source_name": meta["source_name"],
            "url": meta["url"],
            "distance": dist,
        }
        for text, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        )
    ]

    for chunk in chunks:
        print(f"[{chunk['source_name']}] (dist: {chunk['distance']:.3f}) {chunk['text'][:80]}...")

    return chunks
