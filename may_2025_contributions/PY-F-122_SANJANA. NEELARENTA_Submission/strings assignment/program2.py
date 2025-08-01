#Check whether a string is palindrome or not (e.g., "madam").

#program 2

# Get input from the user
input_string = input("Enter a string: ")

# Convert the string to lowercase for case-insensitive comparison
cleaned_string = input_string.lower()

# Check if the string is a palindrome
if cleaned_string == cleaned_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')