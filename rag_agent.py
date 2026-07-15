from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


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

    # =======
    # groq
    # =========

    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)
    print(type(response))
    print(response)

    answer = response.choices[0].message.content

    return answer

