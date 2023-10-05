def solution(a, b, c):
    cnt=0
    if a != b != c != a:
        cnt += a+b+c
    elif a==b==c:
        cnt += (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        cnt += (a+b+c)*(a**2+b**2+c**2)
    return cnt