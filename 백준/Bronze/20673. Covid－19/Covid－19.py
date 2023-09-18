# 20673 Covid-19

# 하루 신규 확진수의 평균
p = int(input())
# 하루 신규 입원수의 평균
q = int(input())
if p<=50 and q<=10:
    print('White')
elif q>30:
    print('Red')
else:
    print('Yellow')