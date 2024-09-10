def solution(array):
    answer = 0
    cnt = [0] * (max(array)+1)
    for i in array:
        cnt[i] += 1
    maxcnt = max(cnt)
    
    if cnt.count(maxcnt) > 1:
        answer = -1
        return answer
    else:
        answer = cnt.index(maxcnt)
        return answer
    
    
    







