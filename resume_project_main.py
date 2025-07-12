# from Load_Resume.doc_loader import doc_loader
# from Chunks.split_text import split_text
# from Create_embedding.open_ai_embedding import open_ai_embeddings
# from Vector_DB.chromadb import create_chroma_db,retriever
# from langchain.chains import create_retrieval_chain
# from LLM.Define_llm import call_llm
# resume=doc_loader("/home/sangram/python_pratice/llm/test_llm/my_resume_project/Uploaded_Resume/Resume_sangram_SR_Manager_latest2025.pdf")
# resume_after_chunks=split_text(500,30,resume)
# embedding=open_ai_embeddings()
# persistent_path_vectordb='/home/sangram/python_pratice/llm/test_llm/my_resume_project/Persistance_loaction'
# vector_store=create_chroma_db(persistent_path_vectordb,embedding,resume_after_chunks)
# retriever = vector_store.as_retriever(search_type="similarity")
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains import create_retrieval_chain
# ########Fewshot prompting ##################
# from Prompting.few_shot_prompting import resume_parser_few_shot_prompt
# from Prompting.prefix_suffix import section_example
# # final_prompt_for_llm = resume_parser_few_shot_prompt().invoke({"resume_text": resume,"section_guidance":section_example()})
# print("--- Final Prompt Sent to LLM ---")
# # print(final_prompt_for_llm.text)

# document_qa_chain = create_stuff_documents_chain(
#     llm=call_llm() , # Low temp for consistent extraction
#     prompt=resume_parser_few_shot_prompt()
# )
# resume_parser_retrieval_chain = create_retrieval_chain(retriever, document_qa_chain)
# # response = resume_parser_retrieval_chain.invoke({"resume_text": resume,"section_guidance":section_example()})

# # The 'answer' key in the response will contain the LLM's parsed output
# # print(response["answer"])
# response = resume_parser_retrieval_chain.invoke({"input": "List the main section of resume"})
# print("\n--- Example: Asking for a specific section after parsing ---")

# # question_answer_chain = create_stuff_documents_chain(
# #     llm=call_llm(),
# #     prompt=prompt,
# # )
# print("\n--- Parsed Resume Output ---")
# print(response["answer"])
# # rag_chain = create_retrieval_chain(retriever, question_answer_chain)


# # response = rag_chain.invoke({"input": "Please list heading of shared resume"})
# # res = response["answer"]

# # print(res)


import os
# from getpass import getpass

# # Set up OpenAI API key (ensure this is at the very top or in a config)
# if "OPENAI_API_KEY" not in os.environ:
#     os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")

# Import your modularized functions
from Load_Resume.doc_loader import doc_loader
from Chunks.split_text import split_text
from Create_embedding.open_ai_embedding import open_ai_embeddings
from Vector_DB.chromadb import create_chroma_db
from LLM.Define_llm import call_llm

# Import LangChain components
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Import your few-shot prompt function
from Prompting.few_shot_prompting import resume_parser_few_shot_prompt

# Define the paths for both resume files
# IMPORTANT: Adjust these paths to where your files are actually located on your system.
resume_paths = [
    "/home/sangram/python_pratice/llm/test_llm/my_resume_project/Uploaded_Resume/Resume_sangram_SR_Manager_latest2025.pdf",
    "/home/sangram/python_pratice/llm/test_llm/my_resume_project/Uploaded_Resume/Khatri_Ravi_CV_Infra.pdf"
]

# Initialize common components outside the loop if they don't change per resume
embedding = open_ai_embeddings()
llm_model = call_llm() # Initialize LLM once

# Get the few-shot prompt template once
full_parsing_prompt = resume_parser_few_shot_prompt()


print("--- Starting Resume Parsing for Multiple Resumes ---")

for i, resume_path in enumerate(resume_paths):
    print(f"\n--- Processing Resume {i+1}: {os.path.basename(resume_path)} ---")

    try:
        # --- 1. Load Resume ---
        # doc_loader expects a file path
        resume_docs = doc_loader(resume_path)
        if not resume_docs:
            print(f"Warning: No documents loaded from {os.path.basename(resume_path)}. Skipping.")
            continue
        print(f"Loaded {len(resume_docs)} document(s) from {os.path.basename(resume_path)}")

        # --- 2. Chunk Resume ---
        resume_after_chunks = split_text(500, 100, resume_docs)
        if not resume_after_chunks:
            print(f"Warning: No chunks generated for {os.path.basename(resume_path)}. Skipping.")
            continue
        print(f"Split resume into {len(resume_after_chunks)} chunks.")

        # --- 3. Create/Load Chroma DB for the current resume ---
        # It's recommended to use a unique path or reinitialize for each resume
        # For simplicity, we'll recreate it each time, or you could manage persistent paths uniquely
        persistent_path_vectordb = f'/home/sangram/python_pratice/llm/test_llm/my_resume_project/Persistance_loaction_{i}'
        vector_store = create_chroma_db(persistent_path_vectordb, embedding, resume_after_chunks)
        print(f"Chroma DB created/loaded for current resume at {persistent_path_vectordb}.")

        # --- 4. Define Retriever ---
        # Ensure 'k' is large enough to fetch all relevant chunks for the parsing task.
        # Adjust based on the expected number of chunks for a single resume.
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": len(resume_after_chunks) * 2})
        print(f"Retriever set up to fetch up to {len(resume_after_chunks) * 2} chunks.")

        # --- 5. Build the Document Combining Chain ---
        # This part reuses the already initialized llm_model and full_parsing_prompt
        document_qa_chain = create_stuff_documents_chain(
            llm=llm_model,
            prompt=full_parsing_prompt
        )
        print("Document combining chain created for current resume.")

        # --- 6. Build the Retrieval Chain ---
        resume_parser_retrieval_chain = create_retrieval_chain(retriever, document_qa_chain)
        print("Retrieval chain for current resume parsing created.")

        # --- 7. Invoke the Chain to Parse the Resume ---
        print("\n--- Initiating Parsing for current resume ---")
        response = resume_parser_retrieval_chain.invoke({"input": "Parse the entire resume and extract 'Academic and Professional Qualification' for 'sangram singh'."})

        print("\n--- Parsed Resume Output ---")
        print(response["answer"])

    except Exception as e:
        print(f"An error occurred while processing {os.path.basename(resume_path)}: {e}")

print("\n--- All Resumes Processed ---")