x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
z = int(input("Enter z value: "))

if x < y and \
   y < z and \
   x + y + z < 100:
    print("All conditions are True")
else:
    print("One or more conditions are False")
