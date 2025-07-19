try:
    x = 10 / 0
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("This will always execute")
