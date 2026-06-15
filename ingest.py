import os
from config import DOCS_PATH


def load_documents():
    """Load all .txt documents from the docs folder."""
    documents = []
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            lines = text.splitlines()
            source_name = lines[0].replace("Source: ", "").strip() if len(lines) > 0 else filename
            url = lines[1].replace("URL: ", "").strip() if len(lines) > 1 else ""

            documents.append({
                "source_name": source_name,
                "url": url,
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} document(s): {[d['source_name'] for d in documents]}")
    return documents


def chunk_document(text, source_name, url):
    """
    Split a restaurant document into chunks ready for embedding.

    Strategy: character-based sliding window with overlap.
      - chunk_size = 200 characters: sized to fit individual restaurant
        reviews, which range from a sentence or two to a short paragraph
      - overlap = 50 characters: preserves context at chunk boundaries so
        a review that spans two chunks can still be retrieved intact
      - min_length = 40 characters: filters out whitespace artifacts,
        section headers, and punctuation fragments with no semantic signal

    Returns a list of dicts, each with:
      - "text"        : the chunk text (str)
      - "source_name" : the source name, e.g. "Eating The Ave" (str)
      - "chunk_id"    : a unique identifier, e.g. "eating_the_ave_0" (str)
      - "url"         : the source URL (str)
    """
    chunk_size = 200
    overlap = 50
    min_length = 40

    chunks = []
    prefix = source_name.lower().replace(" ", "_")
    counter = 0

    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "source_name": source_name,
                "chunk_id": f"{prefix}_{counter}",
                "url": url,
            })
            counter += 1

        start += chunk_size - overlap
    return chunks
