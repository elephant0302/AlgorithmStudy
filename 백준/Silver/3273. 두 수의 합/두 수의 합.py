import math
import sys

lst = []
cnt = 0

n = int(input())
left = 0
right = n-1

lst = list(map(int, sys.stdin.readline().split()))
x = int(input())

lst.sort()

while left < right:
    tmp = lst[left] + lst[right]

    if tmp == x:
        cnt += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1

print(cnt)

