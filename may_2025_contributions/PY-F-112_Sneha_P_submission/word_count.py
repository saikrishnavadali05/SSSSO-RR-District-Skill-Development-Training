import sys
import string
from collections import Counter

def puncremovedtext(text):
    # Remove punctuation and convert them to lowercase
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def countwords(text):
    # Splits the text into a list of words and returns a Counter object (dictionary)
    cleanedtext = puncremovedtext(text)
    words = cleanedtext.split()
    return Counter(words)

def displayscount(wordcounts):
    print(f"{'Word':<10}Count") #Left align the word in a column of 10 characters
    print("-" * 15) # Draw a seperator line with '-'
    for word, count in wordcounts.most_common():  # Sort by frequency from highest to lowest
        print(f"{word:<10}{count}") #Prints each word left aligned by 10 spaces and the word count.

def main():
    if len(sys.argv) < 2: #Give the script name (word_count.py), and filename (ConversationwithSwami.txt)
        print("Usage: python word_count.py ConversationwithSwami.txt") 
        return
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read() #Reads the file
            wordcounts = countwords(text) #Processes the text and counts word frequencies
            displayscount(wordcounts) #Prints the word counts in a table format
    except FileNotFoundError:
        print(f"File not found: {filename}") #If file doesn't exist then this error message is printed

    except Exception as e:
        print(f"An error has occurred: {e}") #Captures and prints any exception

if __name__ == "__main__":
    main()   #Calls main to start the program