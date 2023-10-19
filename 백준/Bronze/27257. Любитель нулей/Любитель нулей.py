# 27257 Любитель нулей
n = input()
cnt = 0 
for i in range(len(n)-1,-1,-1):
    if n[i] == '0':
        cnt += 1
    else:
        break
answer = n[:len(n)-cnt]
print(answer.count('0'))