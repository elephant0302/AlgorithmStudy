import sys
 
n = int(sys.stdin.readline())

ans = []

for i in range(n):
    [x,y] = map(int,sys.stdin.readline().split())
    ans.append([x,y])

ans.sort()
for i in ans:
    print(i[0], i[1])