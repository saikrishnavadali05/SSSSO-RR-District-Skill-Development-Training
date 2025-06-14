# 1. Importing built-in module
import math
print("Square root of 16 is:", math.sqrt(16))

# 2. Import specific value from a module
from math import pi
print("Value of pi is:", pi)

# 3. Use dir() to list module functions
print(math.pi)
print(pi * 8)

# 4. Import with alias
import math as m
print("Factorial of 5 is:", m.factorial(5))

# 5. Run code only if script is directly run
if __name__ == "__main__":
    print("This script is being run directly")

# ✅ 6. Generate 5 random integers (fixed by adding import)
import random
random_nums = [random.randint(1, 10) for _ in range(5)]
print("Random numbers:", random_nums)

# 7. Use custom greet module
import greet
greet.hello()

# 8. Use custom math_ops module
import math_ops
print("Addition:", math_ops.add(5, 3))
print("Multiplication:", math_ops.mul(4, 2))

# 9. Use check_number module to validate input
from check_number import validate_number
try:
    validate_number("abc")  # This will raise ValueError
except ValueError as e:
    print("Error:", e)
