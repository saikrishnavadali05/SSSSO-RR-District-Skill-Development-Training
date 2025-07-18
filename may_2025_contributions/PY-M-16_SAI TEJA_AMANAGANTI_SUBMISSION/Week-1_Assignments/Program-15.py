
'''Question 15:
pylint basics
Create a script with one variable named badly (like X) and run pylint to see the warning. 
Rename it to follow lowercase_style and rerun pylint.
'''
#solution:
#used command prompt to check the linting score 
import pylint


X="hello"
print(X) #for this the score is 0
New_x_value="hello"
print(New_x_value) #for this the score is 10