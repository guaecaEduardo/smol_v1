from smolagents import tool
import os

@tool
def toolApplyCodeFix(file_path: str, fix: str) -> dict:
    """
    Applies a fix directly into the specified file.

    Args:
        file_path: The path to the file to modify.
        fix: The proposed fix.

    Returns:
        dict: Status message and file path.
    """
    try:
        # ✅ Ensure it's targeting the real project directory
        project_root = os.path.join(os.getcwd(), "realproject")
        target_file = os.path.join(project_root, file_path)

        if not os.path.exists(target_file):
            print(f"🚨 File not found: {target_file}")
            return {"status": "failed"}

        with open(target_file, "r", encoding="utf-8") as f:
            code = f.read()

        # ✅ Add fix at the top for now — more control can be added later
        new_code = f"# FIX APPLIED:\n# {fix}\n\n{code}"

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(new_code)

        print(f"✅ Fix applied to {target_file}")

        return {"status": "success", "file_path": target_file}

    except Exception as e:
        print(f"🚨 Error in toolApplyCodeFix: {e}")
        return {"status": "failed"}
