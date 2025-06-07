#Write a Python program to get the first and last character of a string.

# Get input from the user
input_string = input("Enter a string: ")

# Check if the string is not empty
if len(input_string) > 0:
    first_char = input_string[0]
    last_char = input_string[-1]
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
else:
    print("The string is empty.")
