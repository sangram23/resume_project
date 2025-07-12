from langchain_community.document_loaders import PyPDFLoader
import os
def doc_loader(doc_path):
      print(doc_path)
      loader = PyPDFLoader(doc_path)
      documents = loader.load()
      return documents

# doc_loader("../Uploaded_Resume/Resume_sangram_SR_Manager_latest2025.pdf")
# doc_loader("/home/sangram/python_pratice/llm/test_llm/my_resume_project/Uploaded_Resume/Resume_sangram_SR_Manager_latest2025.pdf")
