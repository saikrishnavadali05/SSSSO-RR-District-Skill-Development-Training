from textblob import TextBlob

paragraph = """Python is a widely used programming language. It is easy to learn and has many libraries. Python is great for data science, AI, and web development."""

blob = TextBlob(paragraph)
summary = ' '.join(blob.sentences[:2])  # Simple summary: first 2 sentences

print("Summary:", summary)

#Output:
# Summary: Python is a widely used programming Language. It is easy to learn and has many libraries.
