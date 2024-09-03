import sys
input = sys.stdin.read

data = input().strip().split()
for i in data:
    
    i = int(i)
    num = 1
    cnt = 1
    
    while num % i != 0:
        num = num * 10 + 1
        cnt += 1

    print(cnt)