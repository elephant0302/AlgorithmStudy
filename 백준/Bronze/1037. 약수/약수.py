import sys

n = int(input())

nlist = list(map(int,input().split()))

nlist = sorted(nlist)

if n == 1:
    print(nlist[0]*nlist[0])
else:
    print(nlist[0]*nlist[len(nlist)-1])
    