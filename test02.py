from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# Your provided dictionaries
EXAMPLE_SECTION_TITLES = {
    "Executive Summary": (
        "A brief introduction (3-5 lines) at the top of the resume summarizing the candidate's most relevant skills, "
        "achievements, and experiences tailored to the job. Also known as 'Resume Summary' or 'Career Profile'."
    ),
    "Technical Skills": (
        "A list of job-specific tools, technologies, or systems the candidate is proficient in. "
        "Also known as 'Skills', 'Core Competencies', or 'Technical Expertise'."
    ),
    "Organizational Experience": (
        "Detailed history of previous job roles, responsibilities, and achievements within organizations. "
        "Synonyms include 'Work History', 'Employment History', or 'Professional Experience'."
    ),
    "Academic and Professional Qualification": (
        "Education background, degrees, certifications, and licenses relevant to the job. "
        "May appear under headings like 'Education', 'Qualifications', or 'Academic Background'."
    ),
    "Personal Profile": (
        "Personal information such as date of birth, language proficiency, nationality, and other personal traits. "
        "Also found under 'About Me', 'Personal Details', or 'Personal Information'."
    ),
    "Certifications": (
        "Any professional certifications or additional qualifications obtained by the candidate. "
        "Often found under headings like 'Certifications', 'Courses', or 'Professional Development'."
    )
}
section_guidance = "\n".join([f"{k}: {v}" for k, v in EXAMPLE_SECTION_TITLES.items()])
prefix="""
Persona: You are an expert resume parser. Analyze the following resume content and extract all relevant information
Context:
- Use the content directly from the resume.
- **Label each extracted section clearly using the exact bolded section titles provided below.**
- If a section is missing from the resume, but its synonym or equivalent name is present, use that content for the designated section.
- If a section is missing entirely (no content or synonyms found), suggest adding it to the resume.
- If an extra section is present in the resume that doesn't fit the predefined categories, include it in the suggestions.

**Defined Resume Sections and Their Descriptions:**
{section_guidance}

Resume:
---
{resume_text}
Now extract the sections.
 ."""

suffix = """
Goal: parse the section of resume and arrange required output.
"""

# --- Few-Shot Examples for Resume Parsing ---
# These examples will teach the LLM the desired output format and extraction logic.
# Each example should have an 'input_resume' (the resume text) and an 'output_parsed' (the desired parsed result).
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

# Define the example template
# This tells LangChain how each example (input_resume, output_parsed) should be formatted
example_prompt = PromptTemplate(
    input_variables=["input_resume", "output_parsed"],
    template="Resume:\n---\n{input_resume}\n---\nParsed Output:\n{output_parsed}"
)

# Create the FewShotPromptTemplate
resume_parser_few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["resume_text"],  # This is the variable the final prompt will expect
    example_separator="\n\n" # Separator between each example
)

# --- How to use and view the generated prompt ---
# Example Resume Text to Parse
# test_resume_text = """
# Alice Wonderland
# Project Manager
# alice@example.com

# Summary:
# Experienced project manager with a focus on agile methodologies.

# Skills:
# Agile, Scrum, JIRA, Confluence

# Education:
# MBA from Business School (2015)
# """

# Invoke the prompt with your test resume text
from Load_Resume.doc_loader import doc_loader
test_resume_text=doc_loader("/home/sangram/python_pratice/llm/test_llm/my_resume_project/Uploaded_Resume/Resume_sangram_SR_Manager_latest2025.pdf")
final_prompt_for_llm = resume_parser_few_shot_prompt.invoke({"resume_text": test_resume_text,"section_guidance":section_guidance})

print("--- Final Prompt Sent to LLM ---")
print(final_prompt_for_llm.text)

# Now, you would typically pass final_prompt_for_llm.text to your LLM
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2) # Lower temperature for extraction tasks
# response = llm.invoke(final_prompt_for_llm.text)
# print("\n--- LLM's Parsed Output ---")
# print(response.content)