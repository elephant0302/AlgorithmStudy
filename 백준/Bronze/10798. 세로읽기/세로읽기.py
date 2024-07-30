n = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j<len(n[i]):
            print(n[i][j],end="")
