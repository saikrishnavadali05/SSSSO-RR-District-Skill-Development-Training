import re   #Importing the 're' module for regular expression operations

def normalize_whitespace(text):  #Function to normalize whitespace in a string
    return re.sub(r'\s+', ' ', text).strip()  
      #returns the string with multiple spaces replaced by a string with a single space

print(normalize_whitespace("This    is   python"))
      #prints the normalized string
#Output:
# This is python