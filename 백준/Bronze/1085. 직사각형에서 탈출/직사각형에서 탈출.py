a, b, c, d = map(int, input().split())

answer = []  
answer.append(abs(a - c))
answer.append(abs(b - d))
answer.append(abs(a))
answer.append(abs(b))
your = min(answer)

print(your)