def solution(number, n, m):
    answer = 0
    answer =  int(number%n == 0 and number%m == 0)
    return answer