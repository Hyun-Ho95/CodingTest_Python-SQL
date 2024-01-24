# 1032번 명령 프롬프트(Bronze I)
n = int(input())
cmd = input()
index = []
cmd_list = list(cmd)

for _ in range(n-1):
    cmd_2 = input()
    for idx,k in enumerate(cmd):
        if cmd[idx] == cmd_2[idx]:
            continue
        else:
            index.append(idx)
            
for i in set(index):
    cmd_list[i] = '?'
print(''.join(cmd_list))