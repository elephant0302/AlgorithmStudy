n = []
cnt = 0
mini = 100
result = 0

for i in range(7): 
    n.append(int(input()))
    
for i in n:
    if i % 2 != 0:
        cnt += 1
        if mini > i:
            mini = i
        result += i

if cnt != 0:
    print(result)
    print(mini)
else:
    print(-1)
