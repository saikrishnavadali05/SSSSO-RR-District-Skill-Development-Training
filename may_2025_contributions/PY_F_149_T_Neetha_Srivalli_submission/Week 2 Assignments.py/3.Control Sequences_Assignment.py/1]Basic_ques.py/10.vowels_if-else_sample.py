ch = input("Enter a character: ").lower()   
           #Input is given by the user and converted to lowercase

if ch in 'aeiou':    #Checks if the character is a vowel
    print("Vowel")      #Prints if the character is a vowel
elif ch.isalpha():   #Checks if the character is an alphabet
    print("Consonant")  #Prints if the character is a consonent
else:                #Else condition
    print("Not a valid alphabet character")   #Prints if the character is not a valid alphabet
#Output:
# Enter a character: A
# Vowel
# Enter a character: K
# Consonant