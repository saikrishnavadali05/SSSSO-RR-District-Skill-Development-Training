#Create a set, add two elements to it, and check if a specific element exists in the set.

# Create an empty set
my_set = set()

# Add two elements
my_set.add(10)
my_set.add(20)

# Print the set
print("Set:", my_set)

# Check if a specific element exists
if 10 in my_set:
    print("10 is in the set.")
else:
    print("10 is not in the set.")
