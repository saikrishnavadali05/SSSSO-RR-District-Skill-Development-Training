#23. Write a program that simulates a simple console clock updating every second using carriage return \r.

import time
import datetime

try:
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")
