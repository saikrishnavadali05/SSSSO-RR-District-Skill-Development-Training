"""Print a left-aligned triangle of stars."""

def print_triangle(rows=5):
    """Print a left-aligned triangle with the given number of rows."""
    for i in range(1, rows + 1):
        print('*' * i)

def main():
    """Main function to print the star triangle."""
    print_triangle()

if __name__ == "__main__":
    main()
