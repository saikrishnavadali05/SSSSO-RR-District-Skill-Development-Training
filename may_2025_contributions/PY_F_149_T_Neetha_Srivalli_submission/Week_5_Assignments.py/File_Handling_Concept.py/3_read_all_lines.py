with open("example.txt", "r") as file: #Opens the file in read mode
    lines = file.readlines()    #Reads all lines from the file and stores them in a list
    for line in lines:       #Iterates through each line in the list
        print(line.strip())    #Prints each line 

#Output:
#This will print each line from the file without extra newlines
