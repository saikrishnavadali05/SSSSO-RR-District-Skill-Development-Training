#29.Create a script with user-defined functions, include docstrings, and test their output.
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

def square(x):
    """Returns the square of a number."""
    return x * x

print(greet("Harsha"))
print(f"Square of 5 is {square(5)}")
#output: Hello, Harsha!
#output: Square of 5 is 25
'''Defines two functions with docstrings and calls them.
Greet prints a message; square returns the square.
'''