def solution(num_list):
    answer = 0
    n1 = []
    n2 = []
    for i in num_list :
        if i%2 == 0:
            n1.append(str(i))
        else:
            n2.append(str(i))
                      
    n1 = ''.join(n1)
    n2 = ''.join(n2)
    answer = int(n1) + int(n2)
    return answer