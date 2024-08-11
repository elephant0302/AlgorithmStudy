n = int(input())  # 정수 개수를 입력받습니다.

numbers = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(2,numbers[i]+1):
       if numbers[i] % j == 0:
           if numbers[i] == j:
               cnt += 1
           break

print(cnt)