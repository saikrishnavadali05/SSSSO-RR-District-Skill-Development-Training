basic
import math
print(math.sqrt(16))  # Output: 4.0

import math
print(math.sqrt(25))  # Output: 5.0

import math
print(math.sqrt(16))   # Output: 4.0
print(math.pi)         # Output: 3.141592653589793

intermediate

import math_ops
print("Addition:", math_ops.add(10, 5))              #output:Addition:15
print("Subtraction:", math_ops.sub(10, 5))           #output:Substraction:5    
print("Multiplication:", math_ops.mul(10, 5))        #output:Multiplication:50
print("Division:", math_ops.div(10, 5))              #output:Division:2.0

from math_ops import add, div
print(add(4, 3))   # Output: 7
print(div(10, 2))  # Output: 5.0

import random
random_numbers = [random.randint(1, 10) for _ in range(5)]  #output:Random integers: [3, 7, 1, 10, 5]
print("Random integers:", random_numbers)

Advanced

Without aliases (namespace conflict)
from module_a import greet            #output:Hello from Module B
from module_b import greet
greet()
With aliases (resolved conflict)
from module_a import greet as greet_a   #output:Hello from Module A
from module_b import greet as greet_b   #output:Hello from Module B
greet_a()
greet_b()

import num_check
try:
    print(num_check.add(5, 3))           # Output: 8
    print(num_check.divide(10, 'two'))   # Raises TypeError
except Exception as e:
    print("Error:", e)

import importlib
module_name = "math_ops"
module = importlib.import_module(module_name)  #output:7
result = module.add(3, 4)
print("Result:", result)

import pandas as pd
df = pd.read_csv('data.csv')
print("Data Summary:")
print(df.info())
print("\nStatistics:")
print(df.describe())
avg_salary = df['Salary'].mean()
print(f"\nAverage Salary: ${avg_salary:,.2f}")
older_than_30 = df[df['Age'] > 30]
print("\nPeople older than 30:")
print(older_than_30)
Expected output:
Data Summary:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    5 non-null      object
 1   Age     5 non-null      int64 
 2   Salary  5 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
None
Statistics:
             Age        Salary
count   5.000000      5.000000
mean   31.600000  75400.000000
std     5.862000  28284.271247
min    25.000000  48000.000000
25%    28.000000  60000.000000
50%    30.000000  70000.000000
75%    35.000000  95000.000000
max    40.000000 120000.000000

Average Salary: $75,400.00

People older than 30:
      Name  Age  Salary
2  Charlie   35  120000
4     Evan   40   95000







