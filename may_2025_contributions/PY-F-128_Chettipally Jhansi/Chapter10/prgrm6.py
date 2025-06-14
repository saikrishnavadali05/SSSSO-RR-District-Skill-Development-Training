import os
file_path = 'to_delete.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File does not exist.")
