import os
from google import generativeai as genai
from dotenv import load_dotenv

def main():
    
    try:
    
        load_dotenv()

        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file.")

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel('gemini-2.0-flash')

        prompt = "In one sentence, write a friendly greeting to a new programmer."
        response = model.generate_content(prompt)
        print(response.text)

    except Exception as e:
        
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()