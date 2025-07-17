booleanvalue1 = input("enter the value(True/False)=")
booleanvalue2 = input("enter the value(True/False)=")
booleanvalue1 = booleanvalue1.lower() == "true"
booleanvalue2 = booleanvalue2.lower() == "true"

print("AND=",(booleanvalue1) and (booleanvalue2))
print("OR=",(booleanvalue1) or (booleanvalue2))
print("NOT value1=",not booleanvalue1) 
print("NOT value2=",not booleanvalue2)