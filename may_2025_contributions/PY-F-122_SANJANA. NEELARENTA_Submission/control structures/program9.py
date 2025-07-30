#Write a program to find the sum of all numbers from 1 to n, where n is input from the user.

# Get input from the user
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Add numbers from 1 to n
for i in range(1, n + 1):
    total += i

# Print the result
print(f"The sum of numbers from 1 to {n} is {total}")
