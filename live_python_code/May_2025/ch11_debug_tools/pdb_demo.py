# Example 1: Using pdb
import pdb
x = 10
y = 20
pdb.set_trace() 
# Press 'c' to continue execution, 
# 'n' for next line, 
# 's' to step into function
# 'q' to quit the debugger
# pdb link : https://docs.python.org/3/library/pdb.html

# Using pdb to debug a function
def add(a, b):
    return a + b
print(add(x, y))
