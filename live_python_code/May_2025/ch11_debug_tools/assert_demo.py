# Example 6: Using assert to catch bugs early
def calculate_area(radius):
  assert radius > 0, "Radius must be positive"
  return 3.14 * radius ** 2

# print(calculate_area(5))

print(calculate_area(-5))

# Proper ways to exit a Python script:
# import sys
# sys.exit(0)

# various ways of code Exiting:
# sys.exit(0)  # Exit with status code 0 (success)
# sys.exit(1)  # Exit with status code 1 (error)
# raise SystemExit(0)  # Another way to exit with status code 0
# raise SystemExit(1)  # Exit with status code 1 (error)
# exit(0)  # Exit with status code 0 (success)
# quit()  # Exit the interpreter (equivalent to exit())
# os._exit(0)  # Exit without cleanup (not recommended) 
# import os
# os._exit(0)  # Exit without cleanup (not recommended)
# import os 