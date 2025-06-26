MODULE IN PYTHON:
import math
print(math.sqrt(25))


IMPORT A MODULE:
from math import sqrt, pi
print(sqrt(25))  
print(pi)  


MODULE WITH A ALIAS:
import math as m
print(m.sqrt(36)) 


GENERATE A LIST:
import random
random_numbers = [random.randint(1, 10) for _ in range(5)]
print(random_numbers)


SIGNIFICANCE:
# mypackage/_init_.py
print("mypackage has been imported!")


MATH MODULE:
import math
all_items = dir(math)
functions = [item for item in all_items if callable(getattr(math, item))]
print("Functions in math module:")
for func in functions:
    print(func)


    CUSTOM MODULE:
import validate
try:
    validate.check_is_number(42)
    validate.check_is_number("hello")   
except TypeError as e:
    print("Error:", e)


    IMPORTLIB:
    import importlib
module_name = "math"
math_module = importlib.import_module(module_name)
result = math_module.sqrt(49)
print(f"Square root of 49 is: {result}")


PLUGIN-BASED SYSTEM:
import importlib
import os
PLUGIN_DIR = 'plugins'
def load_and_run(command):
    try:
        module_name = f"{PLUGIN_DIR}.{command}"
        plugin = importlib.import_module(module_name)
        plugin.run()
    except ModuleNotFoundError:
        print(f"Command '{command}' not found.")
    except AttributeError:
        print(f"Command '{command}' does not have a 'run()' function.")
def list_plugins():
    print("Available commands:")
    for f in os.listdir(PLUGIN_DIR):
        if f.endswith(".py") and not f.startswith(""):
            print(f"  - {f[:-3]}")
if _name_ == "_main_":
    list_plugins()
    cmd = input("\nEnter command to run: ")
    load_and_run(cmd)


    SPECIFIC FUNCTION FROM A MODULE:
    from math import sqrt, pow
print(sqrt(16))  
print(pow(2, 3)) 