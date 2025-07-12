from dotenv import load_dotenv
import os
def import_llm_key():
    env_file='/home/sangram/python_pratice/llm/env/.env'
    load_dotenv(env_file)
    api_key = os.getenv('OPENAI_API_KEY')
    print(f"testkey: {os.getenv('OPENAI_API_KEY')}")
    if not api_key:
        print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
    elif not api_key.startswith("sk-proj-"):
        print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
    elif api_key.strip() != api_key:
        print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
    else:      
        print("API key found and looks good so far!")
    return api_key    