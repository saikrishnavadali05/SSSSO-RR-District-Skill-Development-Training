#21.Write a script that accepts command-line input and prints a customized greeting.
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}! Welcome to Python scripting.")
else:
    print("Usage: python greeting.py <YourName>")
#output: Hello, <YourName>! Welcome to Python scripting.
#usage: python greeting.py <YourName>
# Example usage: python greeting.py John
# If no name is provided, it will print the usage message.


