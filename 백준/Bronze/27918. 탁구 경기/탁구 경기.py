# 27918 탁구 경기 
n = int(input())
d = 0
p = 0

for _ in range(n):
    winner = input()
    if winner == 'D':
        d += 1
    else:
        p += 1
    if abs(d-p) >= 2:
        print(f'{d}:{p}')
        break
if abs(d-p) < 2: 
    print(f'{d}:{p}')
