# 27110 특식 배부
n = int(input())
a, b, c = map(int,input().split())
cnt = 0

# 후라이드치킨
cnt += a if a <= n else n
# 양념치킨
cnt += b if b <= n else n
#간장치킨
cnt += c if c <= n else n

print(cnt)