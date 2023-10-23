def solution(numbers, n):
    cnt = 0
    for i in numbers:
        if cnt > n:
            return cnt
        else:
            cnt += i
        
    return cnt