def solution(n):
    
    result = []
    
    for i in range(1,n+1):
        n_divisor = []
        for j in range(1,i+1):
            if i % j ==0:
                n_divisor.append(j)
        if len(n_divisor) >=3:
            result.append(i)
    return len(result)