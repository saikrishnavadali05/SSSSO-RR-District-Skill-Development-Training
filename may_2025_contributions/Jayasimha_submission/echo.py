import sys

# Check if an argument was provided
if len(sys.argv) > 1:
    word = sys.argv[1]
    print(f"You entered: {word}")
else:
    print("No argument provided.")
