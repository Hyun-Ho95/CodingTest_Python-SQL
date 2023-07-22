def solution(box, n):
    
    cnt =1 
    
    for i in box:
        cnt *= (i//n)
        
    return cnt