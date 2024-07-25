s = input()
result = [-1]*26
cnt = 0
for i in s:
    n = ord(i)
    if n>=97 and n<=122 and result[n-97]==-1:
        result[n-97]=cnt
        cnt+=1
    else:
        cnt+=1
        

for i in result:
    print(i,end=" ")