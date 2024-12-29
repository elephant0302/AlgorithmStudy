n = int(input())
a = 0
b = 0
time = list(map(int,input().strip().split()))

for i in time:
    n1 = i//30 + 1
    n1 *= 10
    a += n1
    n2 = i//60 + 1
    n2 *= 15
    b += n2
    


if a == b:
    print(f'Y M {a}')
elif a < b:
    print(f'Y {a}')
else:
    print(f'M {b}')
