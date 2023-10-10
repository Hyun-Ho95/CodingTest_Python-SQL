def solution(n):
    result = []
    while True:
        if n ==1:
            result.append(n)
            break
        else:
            result.append(n)
            if n % 2 ==0:
                n = n / 2
            else:
                n = 3*n +1
    return result