#2. string is palindrome or not 
pal=input("Enter a string:")
if pal==pal[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")