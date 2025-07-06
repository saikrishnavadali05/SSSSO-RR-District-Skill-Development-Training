def custom_format(name, age):    #defining a function with name and age as parameters
    return ("I am {} and I am {} years old.".format(name, age)) 
    #retunrs the formatted string using .foramt() method

print(custom_format("Neetha", 19))  #prints the formatted string by calling the function
#Output:
# I am Neetha and I am 19 years old.