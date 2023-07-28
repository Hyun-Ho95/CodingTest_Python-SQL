# 2530 인공지능 시계
h, m, s = map(int,input().split())
t = int(input())

# 초
s += t % 60
while True:
    if s >= 60:
        s -= 60 
        m += 1
    else:
        break
    
# 분
m += t // 60
while True:
    if m >= 60:
        m -= 60
        h += 1
    else:
        break
# 시
while True:
    if h >=24: 
        h -= 24 # 24보다 크거나 같을 때 h -= 24를 해주는 것은 24로 나눈 나머지값 갖는 것
    else:
        break
print(h,m,s)