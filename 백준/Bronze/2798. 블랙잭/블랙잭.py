n,m = map(int,input().split())

max = 0
card = list(map(int,input().split()))

for i in range(n-2):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = card[i]+card[j]+card[k]
            if m < sum :
                continue
            if max < sum : 
                max = sum

                
print(max)