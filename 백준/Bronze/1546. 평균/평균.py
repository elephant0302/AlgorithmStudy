n = int(input())
x = list(map(int,input().split()))

m = max(x)
sum = 0
for i in x:
    sum += i/m*100
    
print(sum/n)