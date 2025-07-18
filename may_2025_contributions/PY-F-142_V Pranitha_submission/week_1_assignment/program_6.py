'''question 6
Store 0, '', and 42 in a list. Loop through the list and print whether each element is truthy or falsy.

'''
#solution
thelist=[0,'',42]
for value in thelist:
    if value:
        print("{value}truthy")
    else :
        print("{value}Falsy")


