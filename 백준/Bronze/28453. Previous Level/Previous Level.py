# 28453 Previous Level 
n = int(input())
level = list(map(int,input().split()))
result = []
for m in level:
    if m == 300:
        result.append('1')
    elif 275 <= m <300:
        result.append('2')
    elif 250 <= m <275:
        result.append('3')
    else:
        result.append('4')
print(' '.join(result))
    