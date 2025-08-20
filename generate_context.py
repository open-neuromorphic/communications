import os

# --- Configuration ---
ROOT_DIRECTORY = "."  # Start from the current directory
OUTPUT_FILE = "context.txt"
FILE_EXTENSIONS = ['.py', '.md', '.txt', '.toml'] # Add any file types you want to include
EXCLUDE_DIRS = ['.git', '.venv', '__pycache__', 'node_modules']
EXCLUDE_FILES = ['context.txt', 'generate_context.py'] # Don't include the script itself

def generate_context():
    """Finds all specified files, writes their paths and contents to a single file."""

    # 1. Find all relevant file paths
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(ROOT_DIRECTORY):
        # Exclude specified directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

        for filename in filenames:
            # Skip excluded files
            if filename in EXCLUDE_FILES:
                continue

            # Check if the file has one of the desired extensions
            if any(filename.endswith(ext) for ext in FILE_EXTENSIONS):
                full_path = os.path.join(dirpath, filename)
                file_paths.append(full_path)

    file_paths.sort()

    # 2. Write the context file
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            # First, write the directory structure
            outfile.write("--- REPOSITORY STRUCTURE ---\n\n")
            for path in file_paths:
                outfile.write(f"- {path}\n")
            outfile.write("\n" + "="*40 + "\n\n")

            # Second, write the content of each file
            for path in file_paths:
                outfile.write(f"--- START OF FILE: {path} ---\n\n")
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n")
                except Exception as e:
                    outfile.write(f"*** Error reading file: {e} ***\n\n")

        print(f"✅ Successfully generated '{OUTPUT_FILE}' with {len(file_paths)} files.")

    except IOError as e:
        print(f"❌ Error writing to file: {e}")

if __name__ == "__main__":
    generate_context()