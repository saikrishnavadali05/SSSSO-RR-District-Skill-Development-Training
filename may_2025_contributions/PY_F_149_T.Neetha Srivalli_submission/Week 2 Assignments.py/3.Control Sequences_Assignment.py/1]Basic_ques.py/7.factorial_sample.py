num = int(input("Enter a number: "))   #Input is given by the user
factorial = 1   #Variable to store the factorial result
i = 1    #Initialize counter variable

while i <= num:    #Loop from 1 to the number entered by the user
    factorial *= i     #Multiply the current factorial value by the counter
    i += 1     #Increment the counter by 1

print("Factorial is:", factorial)    #Prints the final factorial result
#Output:
# Enter a number: 5
# Factorial is: 120
