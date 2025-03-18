from smolagents import tool

@tool
def toolApplyCodeFix(file_path: str, fix: str) -> dict:
    """
    Applies a fix directly into the specified file.

    Args:
        file_path: The path to the file to modify.
        fix: The fix content to apply.

    Returns:
        dict: Status message and file path.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        # ✅ Add fix at the top for now — more control can be added later
        new_code = f"# FIX APPLIED:\n# {fix}\n\n{code}"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_code)

        print(f"✅ Fix applied to {file_path}")

        return {"status": "success", "file_path": file_path}

    except Exception as e:
        print(f"🚨 Error in toolApplyCodeFix: {e}")
        return {"status": "failed"}
