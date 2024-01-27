# 1010번 다리 놓기(Silver V)
# 1.다이나믹 프로그래밍 사용 X
def factorial(n):
    cnt = 1
    for i in range(1,n+1):
        cnt *= i
    return cnt

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    ans = int(factorial(m) / (factorial(n)*factorial(m-n)))
    print(ans)