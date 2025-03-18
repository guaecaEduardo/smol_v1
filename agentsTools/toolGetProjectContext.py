from smolagents import tool
import json
import os

@tool
def toolGetProjectContext() -> dict:
    """
    Reads and returns the project context from realproject/spec/C1Context.json.

    Returns:
        dict: Context data.
    """
    project_root = os.path.join(os.getcwd(), "realproject")
    context_file = os.path.join(project_root, "spec", "C1Context.json")

    try:
        if not os.path.exists(context_file):
            print(f"🚨 Context file not found: {context_file}")
            return {"context": {}}

        with open(context_file, "r", encoding="utf-8") as f:
            context = json.load(f)

        print(f"✅ Loaded project context from {context_file}")
        return {"context": context}

    except Exception as e:
        print(f"🚨 Error loading project context: {e}")
        return {"context": {}}
