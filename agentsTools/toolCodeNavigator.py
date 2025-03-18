from smolagents import tool
import os

SRC_FOLDER = "realproject/src"
EXCLUDED_FOLDERS = {".git", "venv", "__pycache__", "node_modules"}

@tool
def navigate_code() -> dict:
    """
    Navigates and returns all the project's source code files with paths, 
    including `main.py`.

    Returns:
        dict: A dictionary containing a list of file paths.
    """
    file_paths = []

    # ✅ Get the realproject root
    project_root = os.path.join(os.getcwd(), "realproject")
    src_path = os.path.join(project_root, "src")

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

        # ✅ Add main.py explicitly if it exists
        main_file_path = os.path.join(project_root, "main.py")
        if os.path.exists(main_file_path):
            file_paths.append(main_file_path)
            print(f"✅ Added key file: {main_file_path}")

        print(f"✅ Found {len(file_paths)} Python files.")

    except Exception as e:
        print(f"🚨 Error in navigate_code: {e}")

    return {"files": file_paths}
