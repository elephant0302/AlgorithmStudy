def solution(code):
    answer = ''
    mode = 0
    for i in range(0,len(code)):
        if code[i] == '1' and mode == 0:
            mode = 1
            continue
            
        if code[i] == '1' and mode == 1:
            mode = 0
            continue
            
        if mode == 0:
            if i%2 == 0:
                answer += code[i]

        if mode == 1:
            if i%2 != 0:
                answer += code[i]
                

                
    if answer == '':
        answer = 'EMPTY'
            
    return answer