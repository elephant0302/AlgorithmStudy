n = int(input())
s = [0]*n
for i in range(n):
    s[i] = input()
set_s = set(s)
s = list(set_s)
s.sort()
s.sort(key=len)
for i in s:
    print(i)

    