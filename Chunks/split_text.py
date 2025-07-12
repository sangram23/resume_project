# split documents
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(chunk_size,chunk_overlap,documents):
      text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
      documents = text_splitter.split_documents(documents)
      text_splitter.atransform_documents
      return documents
# from langchain_community.document_loaders import PyPDFLoader
# import os
# def doc_loader(doc_path):
#       print(doc_path)
#       print(os.getcwd())
#       loader = PyPDFLoader(doc_path)
#       documents = loader.load()
#       return documents

# documents=doc_loader("../Uploaded_Resume/Resume_sangram_SR_Manager_latest2025.pdf")
# chunks=split_text(500,10,documents)
# print((chunks[1]))