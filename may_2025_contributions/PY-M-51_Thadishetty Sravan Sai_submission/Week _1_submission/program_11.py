"""Print numbers 1 to 5 separated by commas."""

def main():
    """Print numbers from a list separated by commas."""
    numbers = [1, 2, 3, 4, 5]
    print(*numbers, sep=", ")

if __name__ == "__main__":
    main()
