import csv      #Importing the csv module to handle CSV files

with open("data.csv", newline='') as file:    #Opens the CSV file in read mode
    reader = csv.reader(file)   #Creates a CSV reader object to read the file
    for row in reader:    #Iterates through each row in the CSV file
        print(row)    #Prints each row as a list of values

#Output:
#This will print each row from the CSV file as a list of values