import sys

n = int(input())

cnt = [0] * 10001

for i in range(n):
    cnt[int(sys.stdin.readline())-1] += 1

for i in range(10001):
    if(cnt[i] > 0):
        for j in range(cnt[i]):
            print(i+1)

