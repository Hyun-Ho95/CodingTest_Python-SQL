def solution(num_list):
    
    cnt1 = 1
    cnt2 = (sum(num_list)) **2
    
    for i in num_list:
        cnt1 *= i
    
    return 1 if cnt1<cnt2 else 0