from smolagents import OpenAIServerModel
import os

def get_openai_model():
    return OpenAIServerModel(
        model_id="gpt-4o-mini",
        api_base="https://api.openai.com/v1",
        api_key=os.getenv("OPENAI_API_KEY_1", "your-openai-api-key-here")
    )
