n = int(input())

ns1 = set(map(int,input().split()))

m = int(input())

ns2 = list(map(int,input().split()))


for x in ns2:
    if x in ns1:
        print(1,end=' ')
    else:
        print(0,end=' ')
            