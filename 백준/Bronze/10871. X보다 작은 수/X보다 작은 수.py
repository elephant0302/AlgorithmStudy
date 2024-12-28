a,b = map(int,input().strip().split())

n_list = list(map(int,input().split()))

for i in n_list:
    if i < b :
        print(i, end=" ")
        