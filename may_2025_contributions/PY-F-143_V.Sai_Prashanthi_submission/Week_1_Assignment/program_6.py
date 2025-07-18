''' Question 6:
boolean type
Store 0, '', and 42 in a list. Loop through the list and print whether each element is truthy or falsy.

'''
#solution:
li=[0,'',42] #intialized a list with 0,'',42 as its elements
for i in li: # for loop to loop through list elements
    print(bool(i)) #determining the list element