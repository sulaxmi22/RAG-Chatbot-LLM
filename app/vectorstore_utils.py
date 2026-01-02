# 1. store 
# 2. retrieve in vector database

# we have used faiss vector database 
# but simpler is langchain's inbuilt vector database wrapper faiss
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Storage
# vector db only stores embeddings
def create_faiss_index(texts):
    # create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    # create vector db
    vectorstore = FAISS.from_texts(texts, embedding=embeddings)
    return vectorstore

# 2. Retrieval
def retrieve_similar_docs(vectorstore, query, k=3):
    # retrieve similar docs
    docs = vectorstore.similarity_search(query, k=k)
    return docs