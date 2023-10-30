# 29683Рождественская лотерея
n, a = map(int,input().split())
receipt = list(map(int,input().split()))
cnt = 0 
for i in receipt:
    if i == a:
        cnt += 1
    elif i > a:
        cnt += i//a
print(cnt)