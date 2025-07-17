import os   #Importing the os module to inherit file handling capabilities

print(os.path.exists("myfile.txt"))   #Checks if the file exists
os.remove("myfile.txt")    #Deletes the file if it exists

#Output:
#True
#File deleted.
#File does not exist.