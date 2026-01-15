#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
number = 98
print(f"{number}", end=" ")
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
