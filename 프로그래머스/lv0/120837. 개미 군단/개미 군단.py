def solution(hp): # hp = 23
    
    if hp % 5 ==0:
        cnt = hp // 5 # cnt = 4
    else:
        cnt = hp // 5
        if hp % 5 == 2 or hp % 5 == 4:
            cnt += 2
        elif hp % 5 == 1 or hp % 5 == 3:
            cnt += 1
    
    return cnt