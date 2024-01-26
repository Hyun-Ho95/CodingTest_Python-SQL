#1094번 막대기(Silver V)
x = int(input())
x = bin(x)[2:]
ans = 0

for i in x:
    if i == '1':
        ans += 1
print(ans)