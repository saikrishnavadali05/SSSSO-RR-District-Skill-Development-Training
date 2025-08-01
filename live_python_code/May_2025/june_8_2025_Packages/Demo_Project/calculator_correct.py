from .math_functions import addition
from .math_function_copy import addition_copy

addition_result = addition(5, 3)
addition_copy_result = addition_copy(5, 3)

print(f"Result from math_functions.addition: {addition_result}")
print(f"Result from math_function_copy.addition_copy: {addition_copy_result}")

# If you want to run this python file directly, you should use the following command:
# python -m Demo_Project.calculator_correct
# This ensures that the relative imports work correctly.

# Example Correct Output: python -m Demo_Project.calculator_correct
# PS E:\SSSSO-RR-District-Skill-Development-Training\live_python_code\May_2025\june_8_2025_Packages> python -m Demo_Project.calculator_correct
# This is a copy of the addition function.
# We are in the math_function_copy module.
# .........................................
# Result from math_functions.addition: 8
# Result from math_function_copy.addition_copy: 8

# Example Wrong Command Output: python Demo_Project.calculator_correct
# PS E:\SSSSO-RR-District-Skill-Development-Training\live_python_code\May_2025\june_8_2025_Packages> python Demo_Project.calculator_correct
# C:\Python_3_13\python.exe: can't open file 'E:\\SSSSO-RR-District-Skill-Development-Training\\live_python_code\\May_2025\\june_8_2025_Packages\\Demo_Project.calculator_correct': [Errno 2] No such file or directory
