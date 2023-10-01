# 25640 MBTI
mbti = input()
n = int(input())
cnt = 0
for _ in range(n):
    mbti2 = input()
    if mbti == mbti2:
        cnt += 1
print(cnt)