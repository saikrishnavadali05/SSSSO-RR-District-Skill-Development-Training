import sys
args = sys.argv[1:]
for arg in args:
    if arg.isdigit():
        print(arg, "is a valid integer")
    else:
        print(arg, "is not a valid integer")