# Given two integers (e.g., 5 and 3), print their bitwise AND (&) and OR (`

# Given integers
a, b = map(int, input("Enter two integers separated by space: ").split())

# Bitwise operations
bitwise_and = a & b
bitwise_or = a | b

# Print results
print(f"Bitwise AND of {a} & {b} = {bitwise_and}")
print(f"Bitwise OR of {a} | {b} = {bitwise_or}")
