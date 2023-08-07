def solution(chicken):
    cnt = 0
    while chicken >=10:
        service = chicken // 10
        coupon = chicken % 10
        cnt += service 
        chicken = service + coupon
    return cnt