import sys

n = int(input())

arr = []

for i in range(n):
    j = int(sys.stdin.readline())
    arr.append(j)

arr.sort()

for x in arr:
    print(x)