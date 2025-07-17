#9. Explain the effect of the alarm escape sequence \a and write a program that uses it.

import time

print("Starting countdown...\n")
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("\aTime's up!")  # This triggers the alert sound
