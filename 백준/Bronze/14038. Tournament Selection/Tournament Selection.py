# 14038 Tournament Selection
cnt = 0
for _ in range(6):
    result = input()
    if result == 'W':
        cnt += 1
if 5 <= cnt <=6:
    print(1)
elif 3<= cnt <=4:
    print(2)
elif 1<= cnt <=2:
    print(3)
elif cnt <1:
    print(-1)