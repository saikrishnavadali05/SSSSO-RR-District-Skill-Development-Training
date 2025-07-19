num1 = int(input('enter the frist whole number:'))
num2 = int(input('enter the second whole number:'))
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (division by zero)"
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

