# Develop a program that shows on screen a countdown for the burst of fireworks,
# going from 10 to 0, with a pause of 1 second between them.

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(0.5)

print("BUM! BUM! POOOW!")
