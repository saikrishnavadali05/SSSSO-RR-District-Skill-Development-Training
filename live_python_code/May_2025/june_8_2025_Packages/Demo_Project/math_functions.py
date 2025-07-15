def addition(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtraction(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiplication(a, b):
    """Returns the product of a and b."""
    return a * b

def division(a, b):
    """Returns the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def exponentiation(base, exponent):
    """Returns base raised to the power of exponent."""
    return base ** exponent

def math_print_lines():
    print("Math functions loaded successfully.")
    print("Available functions: addition, subtraction, multiplication, division, exponentiation")
    print("We are in the math_functions module.")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")