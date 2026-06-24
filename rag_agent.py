from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from ollama import chat


def rag_query(question):

    # ==========================
    # Load Vector Database
    # ==========================

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory="vector_db",
        embedding_function=embedding_model
    )

    # ==========================
    # Retrieve Relevant Chunks
    # ==========================

    docs = vectordb.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # ==========================
    # Prompt
    # ==========================

    prompt = f"""
You are an intelligent business assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I could not find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    # ==========================
    # Qwen via Ollama
    # ==========================

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

