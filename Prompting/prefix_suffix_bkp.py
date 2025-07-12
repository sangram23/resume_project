def section_example():
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
    return section_guidance





def prompting_prefix():
    prefix="""
    Persona: You are an expert resume parser. Analyze the following resume content and extract all relevant information
Context:
- Use the content directly from the resume.
- **Label each extracted section clearly using the exact bolded section titles provided below.**
- If a section is missing from the resume, but its synonym or equivalent name is present, use that content for the designated section.
- If a section is missing entirely (no content or synonyms found), suggest adding it to the resume.
- If an extra section is present in the resume that doesn't fit the predefined categories, include it in the suggestions.

**Defined Resume Sections and Their Descriptions:**
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


**Resume to Parse:**
---
{{context}}
---
Now, extract the sections based on the definitions above and present the parsed output, including suggestions.

**Parsed Output:**
"""
    return prefix

def prompting_suffix():
        suffix = ""
        return suffix
