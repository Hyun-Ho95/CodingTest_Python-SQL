# 30045 ZOAC6
n = int(input())
cnt = 0 
for _ in range(n):
    sen = input()
    if '01' in sen or 'OI' in sen:
        cnt += 1
print(cnt)