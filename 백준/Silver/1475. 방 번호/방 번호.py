import math
import sys
n = sys.stdin.readline()
lst = [0]*10

for i in range(10):
    lst[i] = n.count(str(i))
lst[6] = math.ceil( (lst[6] + lst[9]) / 2)
lst[9] = 0

print(max(lst))