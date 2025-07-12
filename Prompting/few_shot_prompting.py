# def resume_parser_few_shot_prompt():
#       from langchain_core.prompts import FewShotPromptTemplate
#       from .prefix_suffix_bkp import prompting_suffix,prompting_prefix
#       from .example_prompt import example_prompt,set_example_to_llm
#       resume_parser_few_shot_prompt = FewShotPromptTemplate(
#             examples=set_example_to_llm(),
#             example_prompt=example_prompt(),
#             prefix=prompting_prefix(),
#             suffix=prompting_suffix(),
#             input_variables=["context"],  # This is the variable the final prompt will expect
#             example_separator="\n\n" # Separator between each example
#             )
#       return resume_parser_few_shot_prompt

# Prompting/few_shot_prompting.py
def resume_parser_few_shot_prompt():
      from langchain_core.prompts import FewShotPromptTemplate
      # Import the specific functions needed
      from .prefix_suffix import prompting_suffix, prompting_prefix, section_example
      from .example_prompt import example_prompt,set_example_to_llm

      # Get the section definitions string first
      section_definitions = section_example()

      # Pass the section definitions string to prompting_prefix
      prefix_content = prompting_prefix(section_definitions) # <--- CHANGE HERE: Pass the definitions

      resume_parser_few_shot_prompt = FewShotPromptTemplate(
            examples=set_example_to_llm(),
            example_prompt=example_prompt(),
            prefix=prefix_content, # <--- Use the content generated with definitions
            suffix=prompting_suffix(),
            input_variables=["context"],  # This is the variable the final prompt will expect from the RAG chain
            example_separator="\n\n" # Separator between each example
            )
      return resume_parser_few_shot_prompt