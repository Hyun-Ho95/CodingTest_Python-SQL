# 21665 미샤와 반전
n,m = map(int,input().split())
char1 = ''
char2 = ''

for _ in range(n):
    char1 += input()
input()
for _ in range(n):
    char2 += input()
cnt = 0

for idx,k in enumerate(char1):
    if char2[idx]==k:
        cnt +=1
print(cnt)