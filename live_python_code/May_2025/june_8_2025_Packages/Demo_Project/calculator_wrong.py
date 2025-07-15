'''
This script is not fit to be used in packages.
The following imports will work correctly only when you run as an individual script.'''

from math_functions import addition
from math_function_copy import addition_copy

addition_result = addition(5, 3)
addition_copy_result = addition_copy(5, 3)

print(f"Result from math_functions.addition: {addition_result}")
print(f"Result from math_function_copy.addition_copy: {addition_copy_result}")

### Command to run this script directly:
# python Demo_Project/calculator_wrong.py

# note: This script is not suitable for use in packages.
# python Demo_Project.calculator_correct