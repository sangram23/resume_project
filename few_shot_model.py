from langchain_core.prompts import FewShotPromptTemplate, FewShotChatMessagePromptTemplate , PromptTemplate,ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
EXAMPLE_SECTION_TITLES = {
    "Executive Summary": (
        "A brief introduction (3–5 lines) at the top of the resume summarizing the candidate's most relevant skills, "
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
{{resume_text}}
---
Now extract the sections.
 ."""
suffix=""" 

Goal: parser the seciton of resume and arrage required output.



"""
# Example - Fixed Few-shot Examples
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondrous wizard of math."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)
# Define the user's input
user_input = "5+7"

# Invoke the final_prompt with the user's input
# This will compile all the components (system message, few-shot examples, human input)
# into a list of message objects.
messages_to_llm = final_prompt.invoke({"input": user_input}).to_messages()

print("--- Final Prompt Messages Going to LLM ---")
for message in messages_to_llm:
    print(f"{message.type.capitalize()}: {message.content}")

# chat = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
# chain = final_prompt | chat
# response = chain.invoke({"input": "What's the square of a triangle?"})

# print(response)