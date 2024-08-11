a,b,c = map(int,input().split())

if sum((a,b,c)) - max((a,b,c)) > max((a,b,c)):
    print(sum((a,b,c)))
else : 
    x = sum((a,b,c)) - max((a,b,c))
    y = max((a,b,c)) - x
    print(sum((a,b,c))-y-1)