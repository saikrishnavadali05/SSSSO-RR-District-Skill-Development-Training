def greet(name):
if name:  # IndentationError: expected an indented block
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")

greet("Alice")