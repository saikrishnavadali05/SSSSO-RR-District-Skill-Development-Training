# Example 1: Using pdb
import pdb # interactive debugger in Python, in-built module
x = 10
y = 20
pdb.set_trace() 
# Press 'c' to continue execution, 
# 'n' for next line, 
# 's' to step into function
# 'q' to quit the debugger
# 'b' to set a breakpoint
# 'l' to list the code around the current line
# 'p' to print a variable's value
# 'h' for help on commands
# pdb link : https://docs.python.org/3/library/pdb.html

# Using pdb to debug a function
def add(a, b):
    return a + b

add_output = add(x, y)
print(add_output)

# import pdb
# x = 10
# y = 20
# pdb.set_trace()
# print(x + y)
