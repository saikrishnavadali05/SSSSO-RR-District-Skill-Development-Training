#21. Write a Python program that reads a string input from the user and replaces all newline escape sequences with a space.

# Read input from the user
user_input = input("Enter a string (with \\n for newlines): ")

# Replace all newline escape sequences with a space
modified_string = user_input.replace("\\n", " ")

# Print the result
print("Modified string:", modified_string)
