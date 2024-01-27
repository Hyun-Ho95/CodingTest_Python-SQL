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

# 2.다이나믹 프로그래밍 사용 O
dp = [[0]*30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i==1:
            dp[i][j] = j
        else:
            if i==j:
                dp[i][j] = 1
            elif i<j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(dp[n][m])
