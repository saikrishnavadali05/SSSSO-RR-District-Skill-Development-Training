# Example 8: Profiling with cProfile
import cProfile
def test():
  total = 0
  for i in range(1000):
    total += i
  return total

cProfile.run('test()') # cprofile will output profiling results to the console

# To save the profiling results to a file, you can use:
cProfile.run('test()', r'E:\SSSSO-RR-District-Skill-Development-Training\live_python_code\May_2025\ch11_debug_tools\cprofiler_demo.prof')

# To view the profiling results, you can use the pstats module:
import pstats
p = pstats.Stats(r'E:\SSSSO-RR-District-Skill-Development-Training\live_python_code\May_2025\ch11_debug_tools\cprofiler_demo.prof')
p.sort_stats('cumulative').print_stats(10)  # Sort by cumulative time and print top 10 functions
