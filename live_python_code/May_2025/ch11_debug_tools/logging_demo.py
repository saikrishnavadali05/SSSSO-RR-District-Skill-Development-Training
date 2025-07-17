# Example 3: Logging instead of print debugging
import logging
logging.basicConfig(level=logging.DEBUG)
x = 5
logging.debug(f"x = {x}")
