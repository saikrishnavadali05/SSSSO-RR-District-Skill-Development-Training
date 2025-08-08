def is_palindrome(s):     #Function to check if a string is a palindrome
    s = s.lower().replace(" ", "")   #Convert to lowercase and remove spaces
    return s == s[::-1]    #Check if the string is equal to its reverse
print(is_palindrome("Sairam"))    

#Output: 
# True