import os
import textwrap
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()
last_id = None
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    #prompt_file = "/Users/vivagupta/Documents/MyPy/venv/chat_with_gpt/codeassist_prompt.txt"
    #prompt_file = "/Users/vivagupta/Documents/MyPy/venv/chat_with_gpt/sentiment_prompt.txt"
    prompt_file = "/Users/vivagupta/Documents/MyPy/venv/chat_with_gpt/idea_assist_prompt.txt"
    global last_id
    
    with open(prompt_file, "r", encoding="utf-8") as f:
        instructions = f.read()

    if last_id:
        response = client.responses.create(model="gpt-4.1", instructions=instructions,input=prompt,previous_response_id = last_id)
    else:
        response = client.responses.create(model="gpt-4.1", instructions=instructions,input=prompt)

    last_id = response.id
    return response.output_text

def main():
    print("\nPlease share your thoughts about ideas you want to build or problems you want to solve")
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ("exit","q","quit"):
            break

        ai_response = get_response(user_input)

        wrapped_text = textwrap.fill(ai_response, width=150)
        print("AI:", wrapped_text)

if __name__ == "__main__":
    main()