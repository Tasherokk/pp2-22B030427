import math
import time

n = int(input())
miliseconds = int(input())
time.sleep(miliseconds / 1000)
print(f"Square root of {n} after {miliseconds} miliseconds is {math.sqrt(n)}")
