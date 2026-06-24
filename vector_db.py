import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# =====================================
# Documents Folder
# =====================================

DOCUMENT_FOLDER = "documents"

documents = []

# =====================================
# Load PDFs
# =====================================

for file in os.listdir(DOCUMENT_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(
            DOCUMENT_FOLDER,
            file
        )

        print(f"Loading: {file}")

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        documents.extend(docs)

# =====================================
# Split Documents
# =====================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(
    documents
)

print(
    f"Total Chunks: {len(chunks)}"
)

# =====================================
# Embedding Model
# =====================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =====================================
# Create Chroma Vector DB
# =====================================

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="vector_db"
)

vectordb.persist()

print("✅ Vector Database Created Successfully")
