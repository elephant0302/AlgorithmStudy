n = []
max = 0
cnt1 = 0
cnt2 = 0
for i in range(9):
    i = list(map(int,input().split()))
    n.append(i)

for i in range(9):
    for j in range(9):
        if max < n[i][j]:
            max = n[i][j]
            cnt1 = i
            cnt2 = j

print(max)
print(cnt1 + 1, cnt2 + 1)