s = list(input())
n = s[::-1]
cnt = 1
for i in range(len(s)):
    if s[i] != n[i]:
        cnt -=  1
        break
print(cnt)