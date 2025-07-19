import os     #Importing the os module to inherit file handling capabilities

if os.path.exists("sample.txt"):   #Checks if the file exists
    os.remove("sample.txt")  #Deletes the file if it exists 
    print("File deleted.")      #Confirmation message after deletion
else:                         #If the file doesn't exist
    print("File does not exist.")  #Prints a message indicating the file does not exist

#Output:
#file deleted.
#File does not exist.
