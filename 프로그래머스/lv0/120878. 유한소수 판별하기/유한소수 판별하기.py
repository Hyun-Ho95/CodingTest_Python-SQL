def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(a, b):
    
    b = b // gcd(a, b)
    
    result = []
    start_num = 2
    while start_num <=b:
        if b % start_num==0:
            result.append(start_num)
            b = b//start_num
        else:
            start_num += 1
        
    for i in result:
        if i not in [2,5]:
            return 2
    return 1
