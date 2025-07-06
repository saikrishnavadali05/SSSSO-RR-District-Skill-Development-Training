a= "apple,banana,grape,orange"    #Giving fruits as string separated by a comma
fruits = a.split(',')    #Splitting the string into a list of fruits using comma

for fruit in fruits:   #iterating through the list of fruits
    print(fruit)   #prints each fruit in a new line
#Output:
# apple
# banana
# grape
# orange