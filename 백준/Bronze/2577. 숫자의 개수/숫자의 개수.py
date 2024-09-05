a = int(input())
b = int(input())
c = int(input())

result = a*b*c

nlist = [0]*10

result = str(result)

for i in range(0,10):
    cnt = 0
    for j in result:
        if i == int(j):
            cnt += 1
    print(cnt)
