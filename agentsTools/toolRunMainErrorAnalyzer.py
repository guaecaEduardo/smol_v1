from smolagents import tool

from models.openai_model import get_openai_model

@tool
async def toolRunMainErrorAnalyzer(error: str, code: str) -> dict:
    """
    Analyzes an error and proposes a fix.

    Args:
        error: The error message produced by the code.
        code: The codebase where the error occurred.

    Returns:
        dict: A dictionary containing the suggested fix.
    """
    model = get_openai_model()  # Load the OpenAI model

    prompt = (
        f"The following codebase:\n{code}\n\n"
        f"Generated this error:\n{error}\n\n"
        f"Analyze the error and propose a fix."
    )
    
    response = await model(prompt)
    suggestion = response.get("choices", [{}])[0].get("text", "").strip()
    
    return {"suggestion": suggestion}
