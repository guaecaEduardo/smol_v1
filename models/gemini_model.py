from openai import OpenAI
from smolagents import OpenAIServerModel
import os

def get_gemini_model():
    return OpenAIServerModel(
        model_id="gemini-1.5-pro",
        api_base="https://generativelanguage.googleapis.com/v1beta/",
        api_key=os.getenv("GEMINI_API_KEY_1", "your-gemini-api-key-here")""
    )


