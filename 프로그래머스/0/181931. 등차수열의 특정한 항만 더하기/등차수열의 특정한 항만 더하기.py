def solution(a, d, included):
    answer = 0
    cnt = 0
    for i in included:
        
        if i == 1:
            answer += a + d*cnt
        cnt += 1
    return answer