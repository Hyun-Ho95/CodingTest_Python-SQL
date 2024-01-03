# 1225번 이상한 곱셈 (Bronze II)
a,b = input().split()

cnt = 0
for i in a:
    cnt += int(i)

ans = 0
for j in b:
    ans += cnt*int(j)

print(ans)
