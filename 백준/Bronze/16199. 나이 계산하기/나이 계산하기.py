# 16199 나이 계산하기
y1, m1, d1 = map(int,input().split())
y2, m2, d2 = map(int,input().split())

count_age = 1 + (y2-y1)
year_age = y2-y1
if m1<m2:
    man_age = y2-y1
elif m1==m2:
    if d1<=d2:
        man_age = y2-y1
    else:
        man_age = y2-y1-1
else:
    man_age = y2-y1-1
print(man_age)
print(count_age)
print(year_age)