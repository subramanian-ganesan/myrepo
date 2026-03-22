import shutil
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python copy_file.py <source> <destination>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except Exception as e:
        print(f"Error copying file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
