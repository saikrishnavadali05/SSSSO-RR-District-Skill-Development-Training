#28.Write a Python script that fails pylint checks, then modify it to score 10.0.
#before fixing pylint errors
a=5
b=6
print(a+b)
#after fixing pylint errors
"""This script adds two numbers and prints the result."""

def main():
    """Main function"""
    a = 5
    b = 6
    print(a + b)

if __name__ == "__main__":
    main()
'''- Original version has no docstring, bad spacing, and no function.
- Fixed version includes docstring, proper formatting, and function usage.'''