from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv
from .import_llm_key import import_llm_key


def call_llm():
      api_key=import_llm_key()
      llm=ChatOpenAI (model="gpt-4o-mini",temperature=0.1)
      return llm
def getllmresponse():
      pass
# query="what is apple"
# llm=call_llm()
# print(llm.invoke(query).content)