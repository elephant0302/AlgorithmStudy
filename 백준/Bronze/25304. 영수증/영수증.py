total = int(input())
n = int(input())
sum=0
for i in range(1,n+1):
    amt, an = map(int,input().split())
    sum += amt*an
    
if total == sum :
    print('Yes')
else :
    print('No')