"""Ask the user for a letter and print whether that letter appears in the word "python"."""

def main():
    """Check if a letter is in the word 'python'."""
    letter = input("Enter a letter: ").lower()

    if letter in "python":
        print(f"Yes, '{letter}' is in the word 'python'.")
    else:
        print(f"No, '{letter}' is not in the word 'python'.")

if __name__ == "__main__":
    main()
