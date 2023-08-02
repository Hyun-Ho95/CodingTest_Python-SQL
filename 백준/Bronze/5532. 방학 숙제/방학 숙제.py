# 5532 방학 숙제
l = int(input()) # 방학 일 수
a = int(input()) # 국어 풀어야하는 페이지
b = int(input()) # 수학 풀어야하는 페이지
c = int(input()) # 하루 최대로 풀 수 있는 국어 페이지
d = int(input()) # 하루 최대로 풀 수 있는 수학 페이지

# 국어 소요 일 수
korean = 0
if a % c ==0:
    korean += a // c
else:
    korean += (a // c) +1
    
# 수학 소요 일 수
math = 0
if b % d ==0:
    math += b // d
else:
    math += (b // d) +1
    
# 놀 수 있는 날
print(l - max(korean,math))