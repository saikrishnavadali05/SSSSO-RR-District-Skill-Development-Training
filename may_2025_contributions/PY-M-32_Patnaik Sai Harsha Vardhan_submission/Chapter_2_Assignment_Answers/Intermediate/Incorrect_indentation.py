#19.Write a script that contains incorrect indentation. Then correct it and explain the changes.
def greet():
print("Hello")   # Incorrect indentation
def greet():
    print("Hello")  # Correct indentation

greet()

'''Issue: 'print' should be indented inside the function.
Fix: Added 4 spaces to align it correctly.'''
