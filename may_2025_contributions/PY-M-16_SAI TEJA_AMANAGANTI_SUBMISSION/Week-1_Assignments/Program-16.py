'''Question 16:
CLI args (very simple)
Use sys.argv to accept one word from the command line and print it back. (Run: python echo.py hello).
'''
#Solution:
#used command prompt to run and when complied without providing any word/input shown error else printed the first word
import sys
if len(sys.argv)>1:
    print(sys.argv[1])
else:
    print("Error")