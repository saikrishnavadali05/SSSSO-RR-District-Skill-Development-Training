# Example 4: Using traceback to get error details
import traceback
try:
  1 / 0
except Exception as e:
  print("Error:", traceback.format_exc())
  print(e)
