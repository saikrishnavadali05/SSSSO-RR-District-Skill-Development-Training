def check_vowel_consonant(s):  
     #Check if the first character is a vowel and the last character is a consonent
    vowels = 'aeiouAEIOU'    #List of vowels
    if s and s[0] in vowels and s[-1].lower() not in vowels and s[-1].isalpha():
    #Checks if the string is not empty, first character is a vowel, last character is a consonent
    # isalpha() checks if the last character is an alphapbet
        return True
           #returns true if the conditions are met
    else:
        return False     
        #returns false if the conditions are not met
print(check_vowel_consonant("Elephant")) 
print(check_vowel_consonant("Banana")) 
#Output:
# True
# False
