import sys

n,m = map(int,input().split())
s = []
check = []

for i in range(n):
    s.append(sys.stdin.readline())

for i in range(m):
    check.append(sys.stdin.readline())

s = set(s)

cnt = 0
for x in check:
    if x in s:
       cnt += 1

print(cnt)