# Python Training 2025 - DataTypes and Variables
# Description : Python program : Create a list of your 3 favorite books.
# Author : Praveena Kumbum
# Date : 23 May 2025


My_Fav_Books = ["Prema Vahini","Dharma Vahini","Dhyana Vahini"]
def List_actions():
    for items in My_Fav_Books:
        print(items)
List_actions()

#finding the length of the string
print("Lenth of the string is : ", len(My_Fav_Books))

#Sorting the items in the list
My_Fav_Books.sort()
print(My_Fav_Books)

#Reversing the items in the list
My_Fav_Books.reverse()
print(My_Fav_Books)

#Appending a value in the list
My_Fav_Books.append("Gita Vahini")
print(My_Fav_Books)

#Removing a item in the list
My_Fav_Books.remove(My_Fav_Books[0])
print(My_Fav_Books)

#Clearing the list values
My_Fav_Books.clear()
print(My_Fav_Books)


# Python Training 2025 - DataTypes and Variables
# Description : Python program : Write a program to check if a number is even or odd using booleans.
# Author : Praveena Kumbum
# Date : 23 May 2025

a = int(input("Please enter the number : "))

is_even = (a % 2 == 0) # This will return a value true or false.

if is_even:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")


# Python Training 2025 - DataTypes and Variables
# Description : Python program : Convert a string "123" into an integer and add 10.
# Author : Praveena Kumbum
# Date : 23 May 2025

Str = "123"
print(f"{int(Str) + 10}")


# Python Training 2025 - DataTypes and Variables
# Description : Python program : Create a dictionary for a student's name, ID, and course.
# Author : Praveena Kumbum
# Date : 23 May 2025
Student_Dict = {
                 "name" : "Veena",
                 "Id" : 54321,
                 "Course" : "Python and Promopt Engineering"
                }
print(Student_Dict)

#Print the key value pairs in the dict
print(Student_Dict.items())

#Updates a value in the dict
Student_Dict.update({"Id" : 87654})

#print only the keys
print(Student_Dict.keys())

#print only the values
print(Student_Dict.values())