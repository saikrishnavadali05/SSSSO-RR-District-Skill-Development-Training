#Write a program to print the multiplication table of a given number using a for loop.

# Get the number from the user
num = int(input("Enter a number: "))

# Print the multiplication table from 1 to 10
print(f"\nMultiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
