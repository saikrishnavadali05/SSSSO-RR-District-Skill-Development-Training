# Example 9: Memory profiling with memory_profiler
# Run using: mprof run script.py and then mprof plot

# pip install memory-profiler

from memory_profiler import profile

@profile
def compute():
  a = [i for i in range(100000)]
  return sum(a)

compute()
