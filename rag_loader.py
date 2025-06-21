from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os

def load_and_embed_all_pdfs(pdf_dir='pdfs', db_dir='vectorstore'):
    """Load all PDFs from a directory, embed them, and save a FAISS vectorstore."""
    docs = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            try:
                loader = PyPDFLoader(os.path.join(pdf_dir, file))
                docs.extend(loader.load())
            except Exception as e:
                print(f"⚠️ Error loading {file}: {e}")

    if not docs:
        print("❌ No valid PDFs found. Skipping embedding.")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(db_dir)
    print("✅ PDF Embedding completed and saved to", db_dir)