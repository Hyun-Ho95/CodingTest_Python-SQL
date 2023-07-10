def gcd(a,b):
    if a % b ==0:
        return b
    return gcd(b, a%b)

def solution(numer1, denom1, numer2, denom2):
    
    #1. 두 분수의 덧셈
    boonja = (numer1 * denom2) + (numer2 * denom1)
    boonmo = denom1 * denom2
    
    #2. gcd 구하기
    gcd_value = gcd(boonja, boonmo)
    
    #3. gcd로 나눈 값 answer에 담기
    answer = [boonja/gcd_value, boonmo/gcd_value]
    return answer