# 1100번 하얀 칸
cnt = 0
for i in range(8):
    line = input()
    for idx,k in enumerate(line):
        if i%2==0 and idx %2 ==0 and k=='F':
            cnt += 1
        elif i%2!=0 and idx %2 !=0 and k=='F':
            cnt += 1
print(cnt)