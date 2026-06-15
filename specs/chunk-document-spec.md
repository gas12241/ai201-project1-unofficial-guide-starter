# Spec: `chunk_document()`

**File:** `ingest.py`
**Status:** Need to fill out.

---

## Purpose

Split a single text document filled with restaurant info into smaller chunks suitable for embedding and semantic retrieval. Each chunk should carry enough context to be meaningful on its own when retrieved in response to a user query.

---

## Input / Output Contract

**Inputs:**

| Parameter     | Type  | Description                                                                              |
| ------------- | ----- | ---------------------------------------------------------------------------------------- |
| `text`        | `str` | The full text of the text document                                                       |
| `source_name` | `str` | Source name, found after "Source: " on the first line of file (e.g., `"Eating The Ave"`) |
| `url`         | `str` | URL, found after "URL: " on the second line of the file                                  |

**Output:** `list[dict]`

Each dict in the returned list contains exactly these keys:

| Key             | Type  | Description                                                                           |
| --------------- | ----- | ------------------------------------------------------------------------------------- |
| `"text"`        | `str` | The chunk text                                                                        |
| `"source_name"` | `str` | The source name (passed through from `source_name`)                                   |
| `"chunk_id"`    | `str` | A unique identifier for this chunk (e.g., `"eating_the_ave_0"`, `"eating_the_ave_1"`) |
| `"url"`         | `str` | The url (passed through from `url`)                                                   |

Returns an empty list `[]` if the input text is empty or produces no valid chunks.

---

## Design Decisions

---

### Splitting approach

```
Character-based sliding window. The document text is stepped through in
fixed-size windows of `chunk_size` characters, advancing by
(chunk_size - overlap) on each step so adjacent chunks share a small
region of text at their boundary.
```

---

### Chunk size

```
200 characters. Reviews aren't very long, they can be as short as a sentence or two,
to as long as a paragraph. Going larger would merge unrelated restaurant reviews
into one chunk, making retrieval harder
```

---

### Overlap

```
50 characters of overlap between adjacent chunks. Some reviews can span longer than
a single chunk, which allows context preservation without bloating the database.
```

---

### Minimum chunk length

```
40 characters. Chunks shorter than this are discarded. Very short segments
typically contain only whitespace, section headers, or punctuation — content
that has no semantic signal and would just add noise to the vector database.
```

---

### Rationale

```
A 200-character window is enough to encapsulate the shorter reviews while not
spliting up bigger reviews into many pieces.
```

---

### Known limitations

```
Character-based splitting is indifferent to sentence and paragraph boundaries.
A chunk can begin mid-sentence or split a review/restaurant across two chunks
even with overlap, if the review is longer than `chunk_size`. Reviews may get
split in the middle of an item. A paragraph-aware or sentence-aware splitter
would handle these cases better, at the cost of more implementation complexity.
```

---

## Implementation Notes

_Fill this in after running the app and confirming ingestion worked._

**Actual chunk count produced across all 8 rule books:**

```
My terminal tells me that after loading 8 rule documents, it stored 149 total
chunks in the vector database.
```

**One thing that surprised you or didn't match your expectations:**

```
I don't know if it's fair to say, but I didn't necesarily have too many expectations.
I guess when I read rule books, I don't think of them being TOO long so the number
of chunks maybe sounds bigger than I thought, but that's about it. Also, I'm kinda curious what 300 characters looks like. In a way it sounds like a lot because it is 300, but I am curious about how long the average rule is in certain rulebooks.
```
