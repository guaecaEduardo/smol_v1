from smolagents import tool
import os

MAX_FILE_SIZE = 100 * 1024  # 100 KB limit per file

@tool
def get_file_source(file_path: str) -> dict:
    """
    Reads the content of a specific Python file.

    Args:
        file_path (str): The path to the Python file.

    Returns:
        dict: A dictionary containing the file content.
    """
    print(f"Tool:get_file_source reading file {file_path}...")

    try:
        if not os.path.exists(file_path):
            print(f"🚨 File not found: {file_path}")
            return {"code": ""}

        if not file_path.endswith(".py"):
            print(f"🚨 Not a Python file: {file_path}")
            return {"code": ""}

        file_size = os.path.getsize(file_path)
        if file_size > MAX_FILE_SIZE:
            print(f"⚠️ File too large ({file_size} bytes) — truncating to {MAX_FILE_SIZE} bytes")

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_FILE_SIZE)  # Truncate large files

        print(f"✅ Loaded file: {file_path}")
        return {"code": content}

    except Exception as e:
        print(f"🚨 Error in get_file_source: {e}")
        return {"code": ""}
