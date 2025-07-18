# Example 3: Logging instead of print debugging
import logging
logging.basicConfig(level=logging.DEBUG)
x = 5
logging.debug(f"x = {x}")

# Various logging levels
logging.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")