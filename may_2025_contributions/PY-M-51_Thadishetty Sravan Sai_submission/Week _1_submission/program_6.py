"""Program 6: Check if items in a list are truthy or falsy."""

items = [0, '', 42]

def main():
    """Main function to print whether items are truthy or falsy."""
    for item in items:
        if item:
            print(f"{repr(item)} is truthy")
        else:
            print(f"{repr(item)} is falsy")

if __name__ == "__main__":
    main()
