# 1159번 농구경기
n = int(input())
player = { chr(i): 0 for i in range(ord('a'),ord('z')+1)}
answer = []

for _ in range(n):
    name = input()
    player[name[0]] += 1

for key,val in player.items():
    if val >=5:
        answer.append(key)

if answer == []:
    print('PREDAJA')
else:
    print(''.join(sorted(answer)))