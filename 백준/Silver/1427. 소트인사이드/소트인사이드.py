n = int(input())
list = []
for i in str(n):
    list.append(i)

list.sort()
list.reverse()
for x in list:
    print(x,end="")