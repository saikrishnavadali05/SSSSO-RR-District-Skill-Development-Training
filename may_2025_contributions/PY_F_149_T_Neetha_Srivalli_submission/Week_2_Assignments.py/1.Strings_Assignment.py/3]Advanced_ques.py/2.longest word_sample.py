def longest_word(sentence):    #Function to find the longest word in a given sentence
    words = sentence.split()    #Splitting the sentence into words
    return max(words, key=len)  
    #max() function returns the longest word based on its length using key=len
print(longest_word("Python is a programming language")) 
#prints the longest word
#Output:
# programming