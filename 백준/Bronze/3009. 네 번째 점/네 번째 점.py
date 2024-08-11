a = []
a.append(0)
for i in range(3):
    x,y = map(int,input().split())
    a.append(x)
    a.append(y)

if a[1] == a[3]:
    a.append(a[5])
elif a[3] == a[5] :
    a.append(a[1])
else : 
    a.append(a[3])


if a[2] == a[4]:
    a.append(a[6])
elif a[4] == a[6] :
    a.append(a[2])
else : 
    a.append(a[4])

print(a[7],a[8])