names = ['Alice', 'Bob', 'Charlie']   #List of names
scores = [85, 90, 95]    #List of scores

combined = list(zip(names, scores))   #Combines names and scores into a list of tuples
print(combined)   #Prints the combined list

#Output:
# [('Alice', 85), ('Bob', 90), ('Charlie', 95)]