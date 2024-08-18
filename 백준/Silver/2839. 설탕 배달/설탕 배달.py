sugar = int(input())

result = 0

while True: 
    if sugar % 5 == 0:
        result += sugar // 5
        break
    if sugar > 5 :
        sugar -= 3
        result += 1
    elif sugar == 3 : 
        result += 1
        break
    else :
        result = -1
        break
        

print(result)