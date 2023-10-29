# 28808 Таблица результатов
n, m = map(int,input().split())
cnt = 0
for _ in range(n):
    word = input()
    for  i in word:
        if i == '+':
            cnt += 1
            break
print(cnt)
    