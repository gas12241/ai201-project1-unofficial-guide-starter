import gradio as gr
from ingest import load_documents, chunk_document
from retriever import embed_and_store, retrieve, get_collection
from generator import generate_response


# ---------------------------------------------------------------------------
# Ingestion — runs once on startup
# ---------------------------------------------------------------------------

def run_ingestion():
    """
    Load restaurant documents, chunk them, and store in ChromaDB.

    If the vector store is already populated, ingestion is skipped.
    To re-ingest (e.g. after changing your chunking strategy), delete the
    ./chroma_db folder and restart the app.
    """
    collection = get_collection()

    if collection.count() > 0:
        print(f"Vector store already populated ({collection.count()} chunks). Skipping ingestion.")
        print("To re-ingest, delete the ./chroma_db folder and restart.")
        return

    print("Ingesting restaurant documents...")
    documents = load_documents()
    all_chunks = []

    for doc in documents:
        chunks = chunk_document(doc["text"], doc["source_name"], doc["url"])
        all_chunks.extend(chunks)

    if all_chunks:
        embed_and_store(all_chunks)
        print(f"Ingestion complete. {len(all_chunks)} chunks stored.")
    else:
        print(
            "\n⚠️  No chunks produced. Make sure chunk_document() is implemented in ingest.py.\n"
            "    The guide will start, but won't be able to answer questions yet.\n"
        )


# ---------------------------------------------------------------------------
# Chat handler
# ---------------------------------------------------------------------------

def chat(message, history):
    if not message.strip():
        return ""
    retrieved = retrieve(message)
    return generate_response(message, retrieved)


# ---------------------------------------------------------------------------
# Gradio UI
# ---------------------------------------------------------------------------

with gr.Blocks(title="UW Restaurant Guide") as demo:

    gr.HTML("""
        <div style="text-align:center; padding:1.25rem 0 0.5rem;">
            <h1 style="font-size:2rem; font-weight:700; color:#065f46; margin:0;">
                🍜 UW Restaurant Guide
            </h1>
            <p style="color:#6b7280; font-size:1rem; margin:0.4rem 0 0;">
                Ask anything about places to eat near the University of Washington.
            </p>
        </div>
    """)

    with gr.Row():
        with gr.Column(scale=3):
            gr.ChatInterface(
                fn=chat,
                # type="messages",
                chatbot=gr.Chatbot(
                    height=440,
                    placeholder=(
                        "<div style='text-align:center; color:#9ca3af; margin-top:3rem;'>"
                        "Ask about restaurants near UW to get started 🍽️"
                        "</div>"
                    ),
                ),
                textbox=gr.Textbox(
                    placeholder='e.g. "Where can I get Thai food near the Ave?"',
                    container=False,
                    scale=7,
                ),
                examples=[
                    "Are there any bakeries you would recommend near Portage Bay?",
                    "I want a Caribbean sandwich near the University of Washington. Any recommendations?",
                    "Can you recommend a Thai restaurant near the University of Washington?",
                    "What pizza places are there near the University?",
                    "I'd like a bagel near the University District, got any ideas?",
                    "Where can I get Korean food near UW?",
                    "What are some cheap places to eat near the Ave?",
                    "Is there anywhere to get sushi near the University of Washington?",
                    "What are some good spots for brunch near UW?",
                ],
                cache_examples=False,
            )

        with gr.Column(scale=1, min_width=180):
            gr.HTML("""
                <div style="background:#ecfdf5; border:1px solid #a7f3d0;
                            border-radius:10px; padding:1rem; margin-top:0.5rem;">
                    <p style="font-size:0.8rem; font-weight:700; color:#065f46;
                               margin:0 0 0.5rem; letter-spacing:0.05em;">
                        📄 LOADED SOURCES
                    </p>
                    <ul style="font-size:0.8rem; color:#047857; list-style:none;
                                padding:0; margin:0; line-height:2;">
                        <li>🗺️ Eater Seattle</li>
                        <li>⭐ TripAdvisor</li>
                        <li>💬 Quora</li>
                        <li>🍽️ OpenTable</li>
                        <li>🚶 Eating The Ave</li>
                        <li>🏆 The Infatuation (Best)</li>
                        <li>🔍 Yelp</li>
                        <li>📰 Seattle Met</li>
                        <li>🏠 Tripalink</li>
                        <li>😌 The Infatuation (Casual)</li>
                    </ul>
                    <hr style="border:none; border-top:1px solid #a7f3d0; margin:0.75rem 0;">
                    <p style="font-size:0.75rem; color:#065f46; margin:0; line-height:1.5;">
                        Answers are grounded in the loaded documents only. If a
                        restaurant isn't in the sources, the guide will say so.
                    </p>
                </div>
            """)


if __name__ == "__main__":
    print("\n" + "="*50)
    print("  UW Restaurant Guide — starting up")
    print("="*50 + "\n")
    run_ingestion()
    demo.launch(theme=gr.themes.Soft(primary_hue="emerald"))
