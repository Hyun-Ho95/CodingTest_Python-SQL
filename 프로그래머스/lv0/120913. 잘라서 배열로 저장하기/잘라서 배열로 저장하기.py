def solution(my_str, n):
    
    result = []
    k = len(my_str) // n
    j = len(my_str) % n 
    
    if j%n==0:
        for idx in range(k):
            result.append(my_str[n*idx:n*(idx+1)])
    else:
        for idx in range(k):
            result.append(my_str[n*idx:n*(idx+1)])
        result.append(my_str[-j:])
    
    return result