lines = ["Hello\n", "This is a file.\n", "Python is fun!\n"] 
#Sample lines to write to a file


with open("output.txt", "w") as file:    #Opens the file in write mode
    file.writelines(lines)   #Writes the list of lines to the file

#Output:
#This will create a file named 'output.txt' with the content from the 'lines' list

