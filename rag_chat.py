from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

def get_answer_from_docs(query, db_dir='vectorstore'):
    try:
        db = FAISS.load_local(db_dir, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        retriever = db.as_retriever()
        qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name="gpt-4o"), retriever=retriever)
        return qa.run(query)
    except Exception as e:
        return f"❌ Failed to retrieve answer: {str(e)}"