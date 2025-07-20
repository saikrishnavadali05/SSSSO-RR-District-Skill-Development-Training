def divide(a, b):     #Function to divide two numbers
    try:            #Try to execute the division
        return a / b     #Retuns the result of the division
    except ZeroDivisionError:      #Catches the exception if division by zero occurs
        return "Error: Division by zero!"   #Retuns an error message

print(divide(10, 2))   #prints the result of dividing 10 by 2
print(divide(10, 0))   #Prints the error message for division by zero

#Output:
#5.0
#Error: Division by zero!