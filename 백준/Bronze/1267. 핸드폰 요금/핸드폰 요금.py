# 1267 핸드폰 요금
n = int(input())

# 영식,민식 요금제
y = 0
m = 0

data = list(map(int,input().split()))

for i in data:
    if i < 30:
        y += 10
    elif 30<= i <60:
        y += 20
    else:
        y += (i//30+1)*10

for j in data:
    if j < 60:
        m += 15
    elif 60<= j <120:
        m += 30
    else:
        m += (j//60+1)*15

if y > m :
    print('M', m)
elif y==m:
    print('Y M', y)
else:
    print('Y', y)