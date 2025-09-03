#!/user/bin/env python3

"""
main_func_sample.py
Author: santhosh uttarapally
Date: 2025-05-18
Description: This program is example for execution code with main function 
"""

def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

def main():
    """This is the main function of the program."""
    user_name = input("Enter your name: ")
    greet(user_name)

if __name__ == "__main__":
    main()