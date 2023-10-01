# 25600 Triathlon
n = int(input())
sol = []
for _ in range(n):
    a, d, g = map(int,input().split())
    if a == d+g:
        sol.append(2*a*(d+g))
    else:
        sol.append(a*(d+g))
print(max(sol))