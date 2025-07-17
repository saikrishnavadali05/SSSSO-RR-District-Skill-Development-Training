my_set = {1, 2, 3}     #Giving values under 'my_set
my_set.add(4)       #adds 4 to the set
my_set.add(5)       #adds 5 to the set

print("Set after adding:", my_set)    #Prints the updated set

if 4 in my_set:                     #Condition
    print("Element 4 exists in the set")   #If condition satisfied,this statement is printed
else:                     #Else condition
    print("Element 4 not found")   #If condition is not satisfied, this statement is printed
#Output:
#Set after adding: (1, 2, 3, 4, 5)
#Element exists in the set