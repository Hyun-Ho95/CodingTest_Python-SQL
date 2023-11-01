# 30008 준영이의 등급
n, k = map(int,input().split())
sub_list = list(map(int,input().split()))
per = []
grade = []

for i in sub_list:
    per.append((i*100)//n)
    
for p in per:
    if 0 <= p <=4:
        grade.append('1')
    elif 4< p <=11:
        grade.append('2')
    elif 11< p <=23:
        grade.append('3')
    elif 23< p <=40:
        grade.append('4')
    elif 40< p <=60:
        grade.append('5')
    elif 60< p <=77:
        grade.append('6')
    elif 77< p <=89:
        grade.append('7')
    elif 89< p <=96:
        grade.append('8')
    else:
        grade.append('9')
print(' '.join(grade))