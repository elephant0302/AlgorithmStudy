n,m = map(int,input().split())
customcase = []

for _ in range(n):
    row = input().strip()
    customcase.append(list(row)) 
        
    
case1 = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"]
]

case2 = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"]
]

result = 1000000

for s in range(n-7):
    for e in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if customcase[s + i][e + j] != case1[i][j]:
                    cnt1 += 1
                if customcase[s + i][e + j] != case2[i][j]:
                    cnt2 += 1

        result = min(result, cnt1, cnt2)

print(result)