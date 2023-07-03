# 25206번 너의 평점은
grade_list = {'A+' : 4.5, 'A0' : 4.0,
              'B+' : 3.5, 'B0' : 3.0,
              'C+' : 2.5, 'C0' : 2.0,
              'D+' : 1.5, 'D0' : 1.0,
              'F' : 0.0 , 'P' : 'null'}
학점 = []
총합 = []
for i in range(20):
    grade = input().split()
    if grade[2] == 'P':
        continue
    else:
        총합.append(float(grade[1]) * float(grade_list[grade[2]]))
        학점.append(float(grade[1]))
print(sum(총합)/sum(학점))