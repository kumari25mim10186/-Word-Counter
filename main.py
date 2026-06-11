"""
Word Counter Project
Author: Your Name
Description: Reads a text file and counts the total number of words.
"""

def count_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        return len(words)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def main():
    print("=" * 40)
    print("      WORD COUNTER APPLICATION")
    print("=" * 40)

    file_path = input("Enter text file name: ")

    result = count_words(file_path)

    if result is not None:
        print(f"\nTotal Words: {result}")


if __name__ == "__main__":
    main()
