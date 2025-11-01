import os
from dotenv import load_dotenv
from google import generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# List and display available models
print("Available Models:")
print("-" * 50)
for model in genai.list_models():
    name = model.name
    methods = model.supported_generation_methods
    print(f"Model: {name}")
    print(f"Supported Methods: {methods}")
    print("-" * 50)