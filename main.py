import sys
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types


def main():
    load_dotenv()

    verbose = False

    args = sys.argv[1:]
    if '--verbose' in args:
        verbose = True
        args.remove('--verbose')

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)
    

def generate_content(client, messages, user_prompt, verbose=False):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print(f"User prompt: {user_prompt}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()