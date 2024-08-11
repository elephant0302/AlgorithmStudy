n = int(input())
d = 2
while(True):
    if n%d != 0:
        d += 1
    else:
        print(d)
        n //= d

    if n == 1:
        break



