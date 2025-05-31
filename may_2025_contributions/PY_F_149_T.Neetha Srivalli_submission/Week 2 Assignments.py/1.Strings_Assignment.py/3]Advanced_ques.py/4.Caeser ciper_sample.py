def caesar_cipher(text, shift):  # Function to encrypt text using caeser cipher
    result = ''    #Empty string to store the encrypted text
    for char in text:   #Iterating through each character in the text
        if char.isalpha():    #checks if the character is an alphabet
            start = ord('A') if char.isupper() else ord('a') 
            #Determines the starting value based on case(uppercase or lowercase))
            result += chr((ord(char) - start + shift) % 26 + start) 
            #Calculating the new characters
        else:
            result += char  #Non-alphabetic characters are added unchanged
    return result   #returns the encrypted text

print(caesar_cipher("Hello World", 3)) #prints the encrypted text