
s = list(input())

n = len(s)
cnt = n
for i in range(n):
    if s[i] == "=" or s[i] == "-":
        cnt -= 1

for i in range(n-1):
    if s[i]+s[i+1] == "lj" or s[i]+s[i+1] == "nj":
        cnt -= 1

for i in range(n-2):
    if s[i]+s[i+1]+s[i+2] == "dz=":
        cnt -=1

print(cnt)