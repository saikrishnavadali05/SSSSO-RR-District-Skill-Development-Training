"""A simple module that calculates the square of numbers."""

def square(n):
    """Calculate the square of a number.
    
    Args:
        n: The number to be squared
        
    Returns:
        The square of the input number
    """
    return n*n

for i in range(1, 6):
    result = square(i)
    print(f"square of {i} is:", result)
