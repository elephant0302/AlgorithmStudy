def solution(num_list):
    answer = 0
    n1 = 1
    n2 = 0
    for i in num_list:
        n1 *= i
        n2 += i
    
    n2 = n2**2
    if n1>n2:
        answer = 0
    else:
        answer = 1
    return answer