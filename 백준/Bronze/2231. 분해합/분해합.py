n = int(input())


for i in range(1,1000001):
    found = False
    m = sum(map(int,str(i)))
    answer = i + m
    if answer == n : 
        found = True
        print(i)
        break
        
if not found :
    print(0)