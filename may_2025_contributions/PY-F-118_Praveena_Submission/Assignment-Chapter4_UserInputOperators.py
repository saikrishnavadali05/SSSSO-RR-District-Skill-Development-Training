# Python Training 2025 - User Inputs and Operators Assignment.
# Description: Write a function that returns the last element of any list without using indexing.
# Author : Praveena Kumbum
# Date : 22 May 2025

#Using indexing - Method 1
States = ["Tamilnadu","Kerala","Andhra Pradesh","Telangana","Maharastra","Kranataka"]

#Displaying all the elements of the list
print("Python program to display the element of the list.")
for State in States:
    print(State)

#Displaying the last element of the list using indexing
print("Last element of the list is : ", States[len(States)-1])

#Displaying last element of the list Without using indexing
def Last_Item_List(States):
    last = None
    for state in States:
        last = state
    return last

print("Last element is :", Last_Item_List(States))


# Python Training 2025 - User Inputs and Operators Assignment.
# Description: Check if the number 17 is prime using comparison and logical operators.
# Author : Praveena Kumbum
# Date : 22 May 2025
x = int(float(input("Please enter the number :")))
if x > 1:
    if x % 2 == 1:
        print(f"{x} is a Prime number.")
    else:
        print(f"{x} is an even number.")
else:
    print("Please eneter a valid number which is grteater than 1")


# Python Training 2025 - User Inputs and Operators Assignment.
# Description: Create a set of vowels present in a given string.
# Author : Praveena Kumbum
# Date : 23 May 2025

Str = input("Please input the string to identify the vowels in it : ")
Vowels = ['a','e','i','o','u']
for letters in Str:
    if letters in Vowels:
        print(f"{letters} is in the vowels set.")


# Python Training 2025 - User Inputs and Operators Assignment.
# Description: Demonstrate the difference between is and == with an example.
# Author : Praveena Kumbum
# Date : 23 May 2025
A = [1,2,3]
B = [1,2,3]
print(A == B) # == compares the values : Returns 'True'
print(A is B) # is compares the memory locations : Returns 'False'
# Here in this program even though set A and B contains the same values the storage memory locations will be differents, hence A is B retuns a false value.