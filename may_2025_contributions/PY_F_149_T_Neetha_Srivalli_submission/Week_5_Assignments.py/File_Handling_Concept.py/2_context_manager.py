
with open('example.txt', 'r') as file:
    content = file.readlines()
    print("File opened safely.")
#Output:
#File opened safely.

#The 'with' block makes sure the file is closed automatically afterwards.

