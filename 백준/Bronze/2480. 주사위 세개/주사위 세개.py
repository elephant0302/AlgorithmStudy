a,b,c = map(int, input().split())

result = 0

if a == b == c :
    print(10000 + 1000*a)
elif a == b :
    print(1000 + 100 * a)
elif c == b :
    print(1000 + 100 * b)
elif a == c :
    print(1000 + 100 * a)
else : 
    print(max(a,b,c)*100)