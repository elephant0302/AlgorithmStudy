def solution(a, b):
    answer = 0
    test1 = int(f"{a}{b}")
    test2 = 2*a*b
    if test1 > test2:
        answer = test1
    else:
        answer = test2
                
    return answer