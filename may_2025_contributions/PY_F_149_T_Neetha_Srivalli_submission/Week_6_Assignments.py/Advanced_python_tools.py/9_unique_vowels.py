sentence = "Python is powerful and fast!"   #Sample sentence
vowels = {char for char in sentence.lower() if char in 'aeiou'} 
               #Set comprehension to find unique vowels in the sentence

print(vowels)  #Prints the set of unique vowels found in the sentence

#Output:
# {'a', 'e', 'i', 'o', 'u'}