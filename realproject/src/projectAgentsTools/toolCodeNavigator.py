from smolagents import tool
import os

SRC_FOLDER = "src"
EXCLUDED_FOLDERS = {".git", "venv", "__pycache__", "node_modules"}

@tool
def navigate_code() -> dict:
    """
    Navigates and returns all the project's source code files with paths.

    Returns:
        dict: A dictionary containing a list of file paths.
    """
    file_paths = []

    # ✅ Get the project root from the current working directory
    project_root = os.getcwd()
    src_path = os.path.join(project_root, SRC_FOLDER)

    try:
        if not os.path.exists(src_path):
            print(f"🚨 Source folder '{src_path}' not found.")
            return {"files": []}

        print(f"🔍 Scanning source folder: {src_path}")

        for root, dirs, files in os.walk(src_path):
            # ✅ Remove excluded folders during traversal
            dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    file_paths.append(file_path)

        print(f"✅ Found {len(file_paths)} Python files.")

    except Exception as e:
        print(f"🚨 Error in navigate_code: {e}")

    return {"files": file_paths}
