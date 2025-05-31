"""import sys
print(sys.argv) 
"""

# echo.py
import sys

# Check if exactly one argument is provided
if len(sys.argv) != 2:
    print("Usage: python arguments.py <word>")
else:
    word = sys.argv[1]
    print(word)