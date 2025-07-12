# Example 9: Memory profiling with memory_profiler
# Run using: mprof run script.py and then mprof plot

# pip install memory-profiler

from memory_profiler import profile

@profile # Decorator to profile the memory usage of the function
def compute():
  # a = [i for i in range(100000)]
  a = [i for i in range(100)]
  return sum(a)

compute()

# Decorator usage:
# @profile
# def function_to_profile():
#     # Function code here
#     pass

# What is a decorator?
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
# It allows you to wrap another function to extend its behavior.
# In Python, decorators are often used for logging, enforcing access control, instrumentation, and caching.
# They are defined using the "@" syntax above the function definition.

# def example_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function call")
#         result = func(*args, **kwargs)
#         print("After the function call")
#         return result

#     return wrapper

# @example_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")    
  
# example_decorator(say_hello)("Alice")