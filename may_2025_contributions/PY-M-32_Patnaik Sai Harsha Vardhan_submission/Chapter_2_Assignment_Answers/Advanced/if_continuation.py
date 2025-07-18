#Use the continuation character in an if-statement condition spanning multiple lines.
x = 5
y = 10
z = 15

if x < y and \
   y < z:
    print("Values are in ascending order.")
#output: Values are in ascending order.

