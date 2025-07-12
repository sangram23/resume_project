# 



# Prompting/prefix_suffix.py
from langchain_core.prompts import PromptTemplate

def section_example():
    # Updated to include section titles from both your resume examples
    EXAMPLE_SECTION_TITLES = {
        "Executive Summary": (
            "A brief introduction (3-5 lines) at the top of the resume summarizing the candidate's most relevant skills, "
            "achievements, and experiences tailored to the job. Also known as 'Resume Summary' or 'Career Profile'."
        ),
        "Technical Skills": (
            "A list of job-specific tools, technologies, or systems the candidate is proficient in. "
            "Also known as 'Skills', 'Core Competencies', or 'Technical Expertise'."
        ),
        "ORGANIZATIONAL EXPERIENCE": ( # Changed to match your exact casing
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
        ),
        # New sections from Khatri_Ravi_CV_Infra.pdf
        "Objective": (
            "A concise statement outlining the candidate's career goals and what they aim to bring to a prospective employer."
        ),
        "Accomplishments": (
            "Key achievements and successes in previous roles, often quantified."
        ),
        "Professional Snapshot": (
            "A brief overview of professional experience and expertise."
        ),
        "Technical Skill Set": (
            "A detailed list of specific technical abilities and proficiencies."
        ),
        "Professional Experience Summary": (
            "A summary of work history, focusing on roles, responsibilities, and key contributions."
        ),
        "Global Certification": (
            "List of international or globally recognized certifications."
        ),
        "Academics": (
            "Educational background, degrees, and academic qualifications."
        )
    }
    section_guidance = "\n".join([f"- **{k}**: {v}" for k, v in EXAMPLE_SECTION_TITLES.items()])
    return section_guidance


def prompting_prefix(section_definitions_str: str):
    prefix = f"""
Persona: You are an expert resume parser. Your task is to analyze the provided resume content, extract ALL relevant information, and organize it into predefined sections.
Your goal is to be exhaustive, precise, and faithful to the original text.

Context:
- You will be provided with the full content of a resume.
- **DEFINITION OF FULL SECTION CONTENT:** A section's content begins immediately after its heading and ends precisely before the start of the next section heading (or the end of the resume if it's the last section).
- **For EVERY identified section, extract its full content based on the definition above.**
- **Do not omit, trim, summarize, paraphrase, or rephrase any part of the extracted content from ANY section.**
- **Provide the text verbatim, respecting all original formatting, line breaks, and whitespace from the resume.**
- **Label each extracted section clearly using the exact bolded section titles provided below.**
- If a section is missing from the resume but its synonym or equivalent name is present, use that content for the designated section.
- If a section is missing entirely (no content or synonyms found), suggest adding it to the resume.
- If an extra section is present in the resume that doesn't fit the predefined categories, include it in the suggestions.

**Defined Resume Sections and Their Descriptions:**
{section_definitions_str}

**Resume to Parse:**
---
{{context}}
---
Now, extract ALL sections based on the definitions above and present the FULL, unedited parsed output for each section, including suggestions for missing or extra sections.

**Parsed Output:**
"""
    return prefix

def prompting_suffix():
        suffix = ""
        return suffix