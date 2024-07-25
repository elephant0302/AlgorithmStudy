dialog = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

a = input()
ret = 0
for j in range(len(a)):
    for i in dialog:
        if a[j] in i:
            ret += dialog.index(i)+3
print(ret)


