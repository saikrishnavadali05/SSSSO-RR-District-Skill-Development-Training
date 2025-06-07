# Ask the user for two whole numbers
num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Handle division carefully to avoid division by zero
if num2 != 0:
    quot_result = num1 / num2
else:
    quot_result = "Undefined (division by zero)"

# Print results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Quotient:", quot_result)
