# Implicit conversion
x = 5
y = 2.5
z = x + y  # x is implicitly converted to float
print("Implicit conversion result:", z, "| type:", type(z))

# Explicit conversion
a = "100"
b = int(a)
print("Explicit conversion result:", b, "| type:", type(b))