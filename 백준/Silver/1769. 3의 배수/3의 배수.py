# 1769번 3의 배수(SilverV)
x = input()
change = 0
while True:
    cnt = 0 
    if len(str(x)) == 1:
        break
    
    for i in str(x):
        cnt += int(i)
    x = cnt
    change += 1

if int(x) %3==0:
    print(change)
    print('YES')
else:
    print(change)
    print('NO')