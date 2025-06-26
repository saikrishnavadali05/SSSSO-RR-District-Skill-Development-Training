def char_frequency(s):   #Defining the function to calculate character frequency
    freq = {}
    for char in s:  #Iterating through each character in the string
        freq[char] = freq.get(char, 0) + 1   #Updating the frequency count of each character
    return freq  #returning the frequency dictionary

print(char_frequency("python"))  #prints the frequency of characters in the string "python"
#Output:
# {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}