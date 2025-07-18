import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}! Welcome to the Python CLI script.")
else:
    print("Hello! Please provide your name as a command-line argument.")
