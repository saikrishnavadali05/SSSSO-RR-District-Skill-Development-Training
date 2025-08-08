from textblob import TextBlob

text = "I love Python. It is very powerful and versatile."
blob = TextBlob(text)

print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

#Output:
# Polarity: 0.5
# Subjectivity: 0.6
