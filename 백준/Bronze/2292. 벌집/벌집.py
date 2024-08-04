
# 6 * n 만큼 더해진다


n = int(input())
a = 1
cnt = 1
while n > a:
    a += 6*cnt
    cnt += 1

print(cnt)