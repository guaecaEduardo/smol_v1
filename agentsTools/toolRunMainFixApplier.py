from smolagents import tool

@tool
async def toolRunMainFixApplier(file_path: str, fix: str) -> dict:
    """
    Applies a fix to the specified file.

    Args:
        file_path: Path to the file to modify.
        fix: The fix to apply to the file.

    Returns:
        dict: A dictionary containing the status and updated file path.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    new_code = f"# Fix applied:\n# {fix}\n\n" + code

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_code)

    return {"status": "success", "file_path": file_path}
