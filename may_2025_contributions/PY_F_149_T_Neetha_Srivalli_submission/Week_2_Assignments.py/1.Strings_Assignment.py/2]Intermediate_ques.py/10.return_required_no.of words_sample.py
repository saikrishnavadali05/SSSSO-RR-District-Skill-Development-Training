def long_words(sentence):     #function to return words with more than 4 characters
    words = sentence.split()    #Splitting the sentence into words
    return [word for word in words if len(word) > 4]  
       #List to return words with length greater than 4 characters
print(long_words("There we go!! We are done"))  #Prints the words with more than 4 characters
#Output:
# ['There' , 'done']