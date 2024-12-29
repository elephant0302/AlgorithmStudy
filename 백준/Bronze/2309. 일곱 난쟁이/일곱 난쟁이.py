n = []
for i in range(9):
    n.append(int(input()))

n.sort()
result_sum = sum(n)

found = False

for i in range(9):
    for j in range(i + 1, 9):
        if result_sum - n[i] - n[j] == 100:
            # 두 개의 숫자를 제외하고 출력
            excluded = {n[i], n[j]}
            for num in n:
                if num not in excluded:
                    print(num)
            found = True
            break
    if found:
        break
