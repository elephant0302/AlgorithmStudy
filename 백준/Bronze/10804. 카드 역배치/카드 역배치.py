n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(10):
    a, b = map(int, input().split())
    tmp = []
    for i in range(a-1,b):
        tmp.append(n[i])
    tmp = list(reversed(tmp)) 
    for i in range(a-1,b):
        n[i] = tmp[i-(a-1)]

for i in n:
    print(i,end=' ')