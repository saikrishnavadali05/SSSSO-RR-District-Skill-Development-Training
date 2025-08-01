#How can you reload a previously imported module without restarting the interpreter?

#import importlib
#importlib.reload(module_name)

#example
#import greet          # First import
#import importlib
#importlib.reload(greet)  # Reloads greet.py without restarting Python

