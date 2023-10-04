def solution(n):
    cnt = 0
    if n % 2 !=0:
        for i in range(1,n+1):
            if i % 2 !=0:
                cnt += i
    else:
        for i in range(1,n+1):
            if i % 2 ==0:
                cnt += i**2
    return cnt