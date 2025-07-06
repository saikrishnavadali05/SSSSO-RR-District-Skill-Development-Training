numbers = [1, 2, 3, 4, 5, 6]  #List of numbers

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 
            #Filters the list to include only even numbers using a lambda function 
print(even_numbers)  #Prints the list of even numbers

#Output:
# [2, 4, 6]
