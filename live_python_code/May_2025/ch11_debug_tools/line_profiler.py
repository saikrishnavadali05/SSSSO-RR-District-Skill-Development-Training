# Example 10: Line profiling with line_profiler
# Use kernprof -l script.py then python -m line_profiler script.py.lprof
from memory_profiler import profile

@profile
def multiply():
  total = 1
  for i in range(1, 100):
    total *= i
  return total

multiply()