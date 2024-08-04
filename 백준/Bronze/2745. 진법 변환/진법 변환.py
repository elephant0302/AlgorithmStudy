a,b = input().split()
c = int(b)
chr = [0]*len(a)
result = 0
for i in range(len(a)):
    if(ord(a[i])>=65 and ord(a[i])<=91):
        chr[i] = ord(a[i]) - 55
    else:
        chr[i] = int(a[i])


for i in range(len(a)):
    result += chr[len(a)-i-1]*(c**i)

print(result)