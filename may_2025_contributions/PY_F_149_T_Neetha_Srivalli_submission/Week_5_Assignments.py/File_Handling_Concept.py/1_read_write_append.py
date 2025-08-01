##'r': Read only – Opens a file for reading. The file must exist for this purpose.
with open('example.txt', 'r') as file:\n content = file.readlines()
#Reads the content of the file line by line and stores it in a list

##'w': Write – Opens a file for writing. If it already exists, it erases it first.
with open('example.txt', 'w') as file:\n file.write('New content')
#Writes 'New content' to the file, erasing any existing content.

##'a': Append – Opens a file for adding to it. The existing content is kept.
with open('example.txt', 'a') as file:\n file.write('Additional content')
#Appends 'Additional content' to the end of the file without erasing existing content.

