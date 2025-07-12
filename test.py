# from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from docx import Document
from LLM.Define_llm import call_llm

# Load resume text from DOCX
def extract_resume_text(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

# Custom prompt template for structured extraction
resume_parser_prompt = ChatPromptTemplate.from_template("""
You are an expert resume parser. Parse the following resume into well-structured sections:
- Executive Summary
- Technical Skills
- Organizational Experience
- Academic and Professional Qualification
- Personal Profile
- Projects (if any)
- Certifications / Awards
- Declaration

Use ONLY the content from the resume. Label each section clearly. If a section is missing, say "Not Mentioned".

Resume:
---
{resume_text}
---
Now extract the sections.
""")

# Build LangChain LLMChain
def build_parser_chain():
    llm =call_llm()##ChatOpenAI(temperature=0, model="gpt-4")
    return LLMChain(llm=llm, prompt=resume_parser_prompt)

# Parse resume using LLM
def parse_resume_llm(docx_path):
    resume_text = extract_resume_text(docx_path)
    chain = build_parser_chain()
    result = chain.run({"resume_text": resume_text})
    return result

# Example run
if __name__ == "__main__":
    resume_path = "/home/sangram/Downloads/Resume_sangram_latest_SRE1.0 (1).docx"
    parsed_output = parse_resume_llm(resume_path)
    print(parsed_output)
