from langchain_openai.embeddings import OpenAIEmbeddings
def open_ai_embeddings():
      # import sys
      # import os
      # sys.path.insert(0,"/home/sangram/python_pratice/llm/test_llm")
      # print(sys.path)
      from  LLM.import_llm_key import import_llm_key 
      model="text-embedding-3-small"
      embeddings=OpenAIEmbeddings(api_key=import_llm_key(),model=model)
      return embeddings