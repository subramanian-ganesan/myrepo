import shutil
import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: python copy_file.py <source> <destination>")
        sys.exit(1)

    source = os.path.join(os.getcwd(), sys.argv[1])
    destination = os.path.join(os.getcwd(), sys.argv[2])

    try:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except Exception as e:
        print(f"Error copying file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
