import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

class generator:
    """using genai from google.generativeai as llm"""
    def __init__(self,model_name = "gemini-1.5-flash"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt:str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    prompt = "What is a cat?"
    generator = generator()
    print(generator.generate(prompt))
