def solution(num_list):
    cnt = 0 
    for i in num_list:
        while True:
            if i==1:
                break
            else:
                if i%2==0:
                    i =i/2
                    cnt += 1
                else:
                    i = (i-1)/2
                    cnt += 1
    return cnt