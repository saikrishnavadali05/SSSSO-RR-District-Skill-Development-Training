from collections import OrderedDict    #importing OrderedDict from collections

ordered = OrderedDict()   
ordered["one"] = 1
ordered["two"] = 2
ordered["three"] = 3    #Creating an OrderedDict with three key-value pairs

print("OrderedDict keys in order:")  #PRints the OrderedDict
for key in ordered:    #Using for loop
    print(key)     #If key is in 'ordered', then it is printed
#Output:
#OrderedDict keys in order:
#one
#two
#three