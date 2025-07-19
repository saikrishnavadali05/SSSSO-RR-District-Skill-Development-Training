import string #Importing the string module to use punctuation
s = "Hello, world! Welcome to Python."    #Giving a string with punctuation
no_punct = "".join(char for char in s if char not in string.punctuation)   
             #Using join() to concatenate characters that are not punctuation
print(no_punct)   #prints the string witout punctuation
#Output:
# Hello world Welcome to python