n = int(input())

n_list = list(map(int,input().split()))
max = n_list[0]
min = n_list[0]
for i in n_list :
    if i > max : 
        max = i
    if i < min : 
        min = i

print(min, max)