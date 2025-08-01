#Print each character in a string using indexing and a loop.

# Get input from the user
input_string = input("Enter a string: ")

# Loop through the string using indexing
print("Characters in the string:")
for i in range(len(input_string)):
    print(f"Character at index {i}: {input_string[i]}")
