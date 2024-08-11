a = int(input())
b = int(input())
answer = 0
cnt = 0
answer2 = 0
for i in range(a,b+1):
    for j in range(2,b+1):
        if i % j == 0:
            if i == j:
                answer += i
                if cnt == 0:
                    answer2 = i
                    cnt += 1
            break

if answer == 0:
    print(-1)
else : 
    print(answer)
    print(answer2)

