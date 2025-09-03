s = "madam"      #Giving a string
if s == s[::-1]:  #checks if the reverse of the string is equal to the original string
               #if it is equal, it is a palindrome and if not, it is not a palindrome
    print("Palindrome")    #Prints if the string is a palindrome
else:
    print("Not a palindrome")  #Prints if the string is not a palidrome
#Output:
#Palindrome