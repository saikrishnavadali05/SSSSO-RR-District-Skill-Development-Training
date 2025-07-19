#program -5
#logical operators
#Read two Boolean values (e.g., True/False) and print the results of and, or, and not on them.

"""Boolean logic operations based on user input."""

def str_to_bool(s):
    """Convert string input to boolean."""
    return s.strip().lower() == "true"

def main():
    """Prompt user for boolean input and perform logical operations."""
    a = str_to_bool(input("Enter first boolean value (True/False): "))
    b = str_to_bool(input("Enter second boolean value (True/False): "))

    print(f"{a} and {b} = {a and b}")
    print(f"{a} or {b} = {a or b}")
    print(f"not {a} = {not a}")
    print(f"not {b} = {not b}")

if __name__ == "__main__":
    main()
