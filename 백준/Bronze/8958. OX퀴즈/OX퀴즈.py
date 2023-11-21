# 8958 OX퀴즈
n = int(input())

for _ in range(n):
    answer = input()
    cnt = 0
    plus = 0
    for i in answer:
        if i == 'O' :
            cnt += 1+(plus*1)
            plus += 1
        else:
            cnt += 0
            plus = 0
    print(cnt)