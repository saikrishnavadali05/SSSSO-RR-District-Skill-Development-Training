def unique_substrings(s, k):  #Function to find unique substrings of lenght k in a string s
    substrings = set()  #Using a set to store unique substrings
    for i in range(len(s) - k + 1):  #Iterates thrigh the string s
        substrings.add(s[i:i+k])  
        #Extracts substring of lenght k from the string s
    return substrings   #Function to find unique substrings of lenght k

print(unique_substrings("Artistic work", 3))  #Prints the unique substrings
#Output:
# {'sti', 'tic', 'Art', 'rti', 'wor', 'ork', 'sti', 'ist', 'sti', 'art', 'tic'}
# {'Art, 'sti', 'ist', 'tic', 'wor', 'ork', 'rti', 'art'}
