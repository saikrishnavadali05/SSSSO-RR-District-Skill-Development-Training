import pandas as pd     #Importing pandas library

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
}                            #Creating a dictionary of lists

df = pd.DataFrame(data)    #Creating a Dataframe from the dictionary

print(df)  #Printing the DataFrame

#Output: 
#       Name  Age
#0     Alice  25
#1     Bob    30
#2    Charlie 22
