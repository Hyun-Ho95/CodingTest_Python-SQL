# 28074 모비스
word = input()
result = ''
for idx,k in enumerate(word):
    if k in 'MOBIS':
        result += k
if len(set(result))==5:
    print('YES')
    
else:
    print('NO')