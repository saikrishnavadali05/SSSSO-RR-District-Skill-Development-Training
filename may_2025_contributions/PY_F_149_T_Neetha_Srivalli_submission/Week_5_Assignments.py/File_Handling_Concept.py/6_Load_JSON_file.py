import json     #Importing the json module to handle JSON data

with open("data.json", "r") as file:    #Opens the JSON file in read mode
    data = json.load(file)     #Loads the JSON data from the file into a python dictionary
    print(data)     #Prints the loaded JSON data

#Output:
#This will print the JSON data as a python dictionary
