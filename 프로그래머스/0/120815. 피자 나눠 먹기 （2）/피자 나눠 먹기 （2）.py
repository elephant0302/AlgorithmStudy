def solution(n):
    
    for i in range(1, n+100):
        get_pizza = i * n
        if get_pizza % 6 == 0:
            break

    return  get_pizza // 6