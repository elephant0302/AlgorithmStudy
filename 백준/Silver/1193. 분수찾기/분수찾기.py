n = int(input())
cnt = 1
while cnt < n:
    n = n - cnt
    cnt += 1


if cnt%2 == 0 :
    print(f"{n}/{cnt-n+1}", end="")
if cnt%2 != 0 :
    print(f"{cnt-n+1}/{n}", end="")






