a=[1,2]      #defining the list a
b=[1,2]      #defining the list b
c=a is b     #a is b is defined under c
                   #This operator checks if both lists refer to the same object
d= (a==b)    #a==b is defined under d
                   #This operator checks if two lists are equal or not
print("result of a is b: ",c)
print("result of a==b: ",d)
#Output:
    #result of a is b: False
    #result of a==b: True