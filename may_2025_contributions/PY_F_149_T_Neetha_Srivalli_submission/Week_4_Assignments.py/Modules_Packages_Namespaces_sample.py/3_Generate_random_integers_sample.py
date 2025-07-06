import random         #Importing a module 'random'

numbers = [random.randint(1, 10) for _ in range(5)] #Any 5 numbers between 1 to 10 are chosen

print("Random numbers :", numbers)  #Prints random numbers
#Output:
#[1, 7, 2, 1, 8]