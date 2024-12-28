def solution(n):
    answer = []
    while True:
        if n == 1:
            answer.append(n)
            break
        if n % 2 == 0:
            answer.append(n)
            n = n/2
        else:
            answer.append(n)
            n = n*3+1
    return answer