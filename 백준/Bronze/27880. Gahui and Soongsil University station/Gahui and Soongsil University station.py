# 27880 Gahui and Soongsil University station
answer = 0
for _ in range(4):
    step_stair , cnts = input().split()
    if step_stair == 'Es':
        answer += int(cnts) * 21
    else:
        answer += int(cnts) * 17
print(answer)