#What does `__name__ == "__main__"` do in a Python script?
#It checks whether the script is being run directly or imported as a module.

#purpose
#If the script is run directly, the code inside runs.
#If the script is imported, the code inside does not run.

#example
## greet.py
#def hello():
#   print("Hello!")

#if __name__ == "__main__":
#   hello()  # This runs only when greet.py is run directly
