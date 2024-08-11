a,b = map(int,input().split())
cnt = 0

for i in range(1,a+1):

    if a%i == 0:
        b -= 1

    if b == 0:
        cnt = i
        break
        
print(cnt)