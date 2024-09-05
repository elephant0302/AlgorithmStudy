import sys
input = sys.stdin.readline

n = int(input())
for x in range(n):
    i = int(input())
    i1 = set(map(int,input().split()))
    j = int(input())
    j2 = list(map(int,input().split()))
    for num in j2:
        if num in i1:
            print(1)
        else:
            print(0)