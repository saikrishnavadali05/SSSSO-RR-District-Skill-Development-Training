# Python Training 2025 - File Handling _ Assignment
# Author : Praveena Kumbum
# Date : 16 Jun 2025


#@@@@@@@@@@@@@@@@@@@@@@@Basic Questions@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#What is the difference between the file modes 'r', 'w', and 'a'?
#r - read mode, reads the file data but fails if file does not exist.
#w - write mode, creates a new file or overwrite the content of an existing file.
#a - append mode, Adds to the end of the file, creates a file if not found.

#How do you open a file using a context manager?
with open('TheWhisperOfFileModes.txt','r') as file:
    content = file.read()
    print(content)

#Write a Python code snippet to read all lines from a text file.
with open('TheWhisperOfFileModes.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

#How can you write a list of strings to a file?
lines = ["Hello friend!","how are you doing?","Where are you going today?"]

with open('TheWhisperOfFileModes','w') as file:
    for line in lines:
        file.write(line + '\n')

with open('TheWhisperOfFileModes','r') as file:
    print(file.read())

#What Python module would you use to handle CSV files?
import csv

with open('output.csv',mode = 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Age','City'])
    writer.writerow(['Samaikya',2,'Hyderabad'])


with open('output.csv', mode = 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#How do you load a JSON file into a Python dictionary?
import json

# Step 1: Write JSON data to the file
with open('data.json', 'w') as file:
    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    json.dump(data, file)  # write dictionary directly to file

# Step 2: Read JSON data back from the file
with open('data.json', 'r') as file:
    data_loaded = json.load(file)

print(data_loaded)


#How do you safely delete a file in Python?
import os

try:
    os.remove('output.csv')
except FileNotFoundError:
    print("File not found.")


#What does the `with open()` statement help prevent?
#Using with open(), automatically closes the open files. Which inturn prevents loss of data due to an opened file.

#Creating and writing data to the file.
with open('data.txt','w') as file:
    file.write("Hello friends.\nHow are you doing?\nWhere have you been since long time?\nFeeling very happy to meet you after a long time.")

#without using with open()
file = open('data.txt','r')
data = file.read()
print(data)
file.close()  # Have to use this extra line of code to close the opened file manually.
print("file closed successfully")


#with using with open()
with open('data.txt','r') as file:
    data = file.read
    print(data)


#Explain the purpose of the `os` module in file handling.

"""os module is used for file and directory operations.

1. Working with File Paths
os.path.exists(path) # Check if a file or directory exists
os.path.join(path1, path2) # Safely join paths across platforms
os.path.abspath(path) # Get the absolute path

2. File and Directory Operations
os.remove(file) # Delete a file
os.rename(src, dst) # Rename or move a file
os.mkdir(path) # Create a new directory
os.rmdir(path) # Remove an empty directory
os.listdir(path) # List files and folders in a directory

3. Environment Interaction
os.getcwd() # Get the current working directory
os.chdir(path) # Change the working directory
os.environ # Access environment variables"""



#How do you append new data to an existing file?

with open('data.txt','r') as file:
    print("\n************Data in the file before appending :*************\n",file.read()) #Reading the file data before appending the file.
    
with open('data.txt','a') as file:
    file.write("\nReply:\nHi Friend.\nI am doing well.Thanks for asking.\nI am in Hyderabad.\nHow have you been.\nEven I feel the same.")

with open('data.txt','r') as file:
    print("\n************Data in the file after appending :************\n",file.read()) #Reading the file post appeding the file.


#@@@@@@@@@@@@@@@@@@@@@@@Intermediate Questions@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""Write a Python code example to read a CSV file and print each row as a dictionary.
How do you convert a Python dictionary into a JSON formatted string and write it to a file?
Explain the difference between reading a file in text mode vs binary mode.
Describe how to handle exceptions when trying to open a non-existent file.
Write a Python snippet to parse an XML file and extract data from a specific tag.
What are the benefits of using the `pathlib` module over `os.path` for file paths?
How would you read a large file without loading it entirely into memory?
Demonstrate how to rename a file using Python.
Write code to merge two CSV files into a single file.
Explain how to check if a file exists before performing operations on it."""