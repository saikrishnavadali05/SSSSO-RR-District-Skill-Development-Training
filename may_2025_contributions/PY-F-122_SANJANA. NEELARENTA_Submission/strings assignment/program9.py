#Check if a substring is present in a given string using in.

# Get input from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

# Use 'in' to check for presence
if substring in main_string:
    print(f"'{substring}' is present in the main string.")
else:
    print(f"'{substring}' is not present in the main string.")
