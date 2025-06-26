from .math_functions import addition
from .math_function_copy import addition as add, addition_copy
a = 10
b = 5
print(addition(a, b))
print(add(a, b))
print(addition_copy(a, b))

# import my_utils wrong way of using modules within a package

from .my_utils import greet
print(greet("John"))