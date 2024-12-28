def solution(arr, queries):
    answer = []
    for a,b,c in queries:
        min = 1000001
        for i in range(a,b+1):
            if arr[i] > c:
                if min > arr[i]:
                    min = arr[i]
        if min == 1000001:
            min = -1
        answer.append(min)
    return answer