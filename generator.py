from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

_client = Groq(api_key=GROQ_API_KEY)


def generate_response(query, retrieved_chunks):
    """
    Generate a grounded answer from retrieved restaurant chunks.

    `retrieved_chunks` is the list returned by retrieve(). Each item is a dict:
      - "text"        : the chunk text
      - "source_name" : the name of the source (e.g. "Eating The Ave")
      - "url"         : the source URL
      - "distance"    : similarity score (lower = more similar for cosine)

    The response answers using only the retrieved context, identifies which
    source the information comes from, and says so clearly when the answer
    isn't found in the loaded documents.

    Returns the response as a plain string.
    """
    if not retrieved_chunks:
        return (
            "I couldn't find anything relevant in the loaded documents. "
            "Try rephrasing your question — or check that your ingestion pipeline is working."
        )

    context = "\n\n".join(
        f"[Source: {chunk['source_name']} | {chunk['url']}]\n{chunk['text']}"
        for chunk in retrieved_chunks
    )

    system_message = (
        "You are a restaurant guide assistant for the University of Washington area. "
        "Answer the user's question using ONLY the restaurant information provided below. "
        "Do not use your general knowledge of restaurants or Seattle, and do not infer "
        "or extrapolate beyond what is explicitly stated in the provided text. "
        "If the answer is not contained in the provided context, say so clearly — do not guess. "
        "Always identify which source your answer comes from."
    )

    user_message = f"Restaurant context:\n\n{context}\n\nQuestion: {query}"

    response = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message.content
