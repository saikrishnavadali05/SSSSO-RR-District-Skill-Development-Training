# # Example 7: Using faulthandler for low-level crashes
# import faulthandler
# faulthandler.enable() # Enable faulthandler to catch crashes

# # Using faulthandler to cause a segmentation fault
# # This function will intentionally cause a segmentation fault
# def cause_segfault():
#     # This will cause a segmentation fault
#     import ctypes
#     ctypes.string_at(0)  # Attempt to read memory at address 
    
# cause_segfault()

import faulthandler
import sys

faulthandler.enable()
faulthandler.dump_traceback(sys.stderr)
