from smolagents import tool

@tool
def update_file(file_path: str, new_content: str) -> dict:
    """
    Overwrites the content of a file.

    Args:
        file_path: The absolute path of the file to update.
        new_content: The new content to write into the file.

    Returns:
        dict: Status of the operation.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"✅ Successfully updated: {file_path}")
        return {"status": "success", "file_path": file_path}

    except Exception as e:
        print(f"🚨 Error updating file '{file_path}': {e}")
        return {"status": "error", "error": str(e)}
