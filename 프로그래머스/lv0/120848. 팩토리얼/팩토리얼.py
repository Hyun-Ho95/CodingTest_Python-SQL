def solution(n):
    
    x = 10
    
    while True:
        cnt = 1
    
        for i in range(1,x+1):
            cnt *= i
        if cnt <= n:
            return x
            break
        else:
            x -= 1