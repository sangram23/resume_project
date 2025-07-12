def set_example_to_llm():
      examples = [
    {
        "input_resume": """
John Doe
Software Engineer
johndoe@email.com | (123) 456-7890

Summary:
Highly motivated Software Engineer with 5 years of experience in developing web applications.

Skills:
Python, Java, SQL, AWS, Docker, Kubernetes

Work Experience:
Software Engineer at TechCorp (2020-Present)
- Developed and maintained backend services.

Education:
B.Tech in Computer Science from University of Example (2016-2020)
""",
        "output_parsed": """
**Executive Summary:**
Highly motivated Software Engineer with 5 years of experience in developing web applications.

**Technical Skills:**
Python, Java, SQL, AWS, Docker, Kubernetes

**Organizational Experience:**
Software Engineer at TechCorp (2020-Present)
- Developed and maintained backend services.

**Academic and Professional Qualification:**
B.Tech in Computer Science from University of Example (2016-2020)

**Suggestions:**
- Consider adding a 'Personal Profile' section for more complete information.
- Consider adding a 'Certifications' section if applicable.
"""
    },
    {
        "input_resume": """
Jane Smith
Marketing Specialist
jane.smith@email.com

About Me:
Creative and results-driven marketing professional with a proven track record.

Experience:
Marketing Coordinator at Global Brands (2018-2023)
- Managed social media campaigns.

Certificates:
Google Ads Certified

Languages: English, Spanish
""",
        "output_parsed": """
**Personal Profile:**
Creative and results-driven marketing professional with a proven track record.
Languages: English, Spanish

**Organizational Experience:**
Marketing Coordinator at Global Brands (2018-2023)
- Managed social media campaigns.

**Certifications:**
Google Ads Certified

**Suggestions:**
- Consider adding an 'Executive Summary' for a quick overview.
- Consider adding a 'Technical Skills' section if applicable.
- Consider adding an 'Academic and Professional Qualification' section if applicable.
"""
    }
]
             
     
      return examples

def example_prompt():
      from langchain_core.prompts import  PromptTemplate
      example_prompt = PromptTemplate(
            input_variables=["input_resume", "output_parsed"],
            template="Resume:\n---\n{input_resume}\n---\nParsed Output:\n{output_parsed}"
            )
      return example_prompt

            
# print(set_example_to_llm('Kid'))            