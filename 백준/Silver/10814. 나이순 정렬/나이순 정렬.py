import sys

n = int(sys.stdin.readline())

lst = []

for i in range(n):
    a,b = sys.stdin.readline().split()
    a = int(a)
    lst.append((a,b))

lst.sort(key = lambda x : x[0])

for i in lst:
    print(i[0], i[1])