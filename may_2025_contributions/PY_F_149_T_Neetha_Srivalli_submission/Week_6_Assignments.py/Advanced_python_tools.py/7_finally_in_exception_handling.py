#'finally' runs no matter what, even if:
        #There was an exception
        #You used return or break inside try or except
try:      #Attempt to execute the following code
    x = 10 / 0    #This will raise a ZeroDivisionError
except ZeroDivisionError:    #Catches the ZeroDivisionError
    print("Caught division error")   #Prints a message indicating the error was caught
finally:     #This block will always execute
    print("This will always run")   #Prints a message indicating this block always runs


#Output:
#Caught division error
#This will always run
