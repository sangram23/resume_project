from langchain_community.vectorstores import Chroma
# from Create_embedding.open_ai_embedding import open_ai_embeddings
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# import chromadb
def create_chroma_db(persits_path,embedding,documents):
      vector_chromadb = Chroma.from_documents(documents=documents, embedding=embedding, persist_directory=persits_path)
      return vector_chromadb

def retriever(vectorstore):
      retriever = vectorstore.as_retriever()
      return retriever

