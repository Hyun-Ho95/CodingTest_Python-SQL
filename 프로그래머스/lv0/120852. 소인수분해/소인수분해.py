def solution(n):
    
    start_num = 2
    prime_factor = []
    
    while start_num <= n:
        if n % start_num==0:
            prime_factor.append(start_num)
            n = n // start_num
        else:
            start_num += 1
    return list(dict.fromkeys(prime_factor))