#   from nltk.corpus import stopwords   --Import necessary modules
#   from nltk.tokenize import word_tokenize  --Import word_tokenize for tokenization

#   nltk.download('stopwords')      --Download stopwords corpus
#   nltk.download('punkt')          --Download punkt tokenizer models
  
#   text = "This is a sample sentence showing off the stop words filtration."
#   words = word_tokenize(text)
#   filtered = [w for w in words if w.lower() not in stopwords.words('english')]

#   print("Filtered Text:", filtered)

#Output:
# Filtered Text: ['sample', 'sentence', 'showing', 'stop', 'words', 'filteration', '.']
