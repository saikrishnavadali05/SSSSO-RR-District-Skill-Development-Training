 
print ("student")
import example
print ("import module")



# with out from 
import math1
a = int(input("enter a value"))
b = int(input("enter b value"))
print (math1.add)
print (math1.sub)
print (math1.mult) #     a = int(input("enter a value"))
                      #     IndentationError: unexpected indent
                    


# import with from 

from math1 import add,sub,mult  
if __name__ == "__main__": #__name__ == "__main__":     # ????                
    a = int(input("enter a value"))
    b = int(input("enter b value"))
#print (add)
    print (add)    
    print (sub)
   # print (mult)

# pre defined functions or modules
import math
import random
import datetime
import os

print(math.sqrt(64))                 # 8.0
print(random.randint(1, 10))         # Random number from 1 to 10
print(datetime.datetime.now())       # Current date and time
print(os.getcwd())                   # get current working directory 


# dir() predefined module 
#import math 

print (dir())

# import with alias name
import math1 as m1                      
a = int(input("enter a value"))
b = int(input("enter b value"))
print (m1.add)
#print (m1.sub)
print (m1.mult)