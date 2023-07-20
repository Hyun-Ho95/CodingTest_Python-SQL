def solution(balls, share):
    
    balls_fac = 1
    for i in range(balls,1,-1):
        balls_fac *= i
        
    share_fac = 1
    for i in range(share,1,-1):
        share_fac *= i
        
    ball_share_fac = 1
    for i in range(balls-share,1,-1):
        ball_share_fac *= i
        
    answer = (balls_fac)/(ball_share_fac * share_fac)
    return int(answer)