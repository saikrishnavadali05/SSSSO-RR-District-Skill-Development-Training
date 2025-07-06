n = int(input("Enter a number: "))    #Input is given by the user
total = 0      #Variable to store the sum

for i in range(1, n + 1):    #Loop from 1 to the number entered by the user
    total += i      #Add the current number to the total

print("Sum is:", total)   #Prints the final sum result
#Output:
# Enter a number: 9
# Sum is: 45
