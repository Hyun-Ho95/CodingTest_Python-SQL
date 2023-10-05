def solution(num_list):
    
    cnt1 = ''
    cnt2 = ''
    
    for i in num_list:
        if i % 2==0:
            cnt1 += str(i)
        else:
            cnt2 += str(i)
    return int(cnt1)+int(cnt2)