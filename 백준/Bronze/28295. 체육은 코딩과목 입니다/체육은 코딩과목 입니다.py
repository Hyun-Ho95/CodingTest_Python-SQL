#28295 체육은 코딩과목 입니다
di = 'N'
for _ in range(10):
    order = int(input())
    if di == 'N' and order ==1:
        di = 'E'
    elif di =='N' and order ==2:
        di = 'S'
    elif di =='N' and order ==3:
        di = 'W'
        
    elif di == 'E' and order ==1:
        di = 'S'
    elif di =='E' and order ==2:
        di = 'W'
    elif di =='E' and order ==3:
        di = 'N'
        
    elif di == 'W' and order ==1:
        di = 'N'
    elif di =='W' and order ==2:
        di = 'E'
    elif di =='W' and order ==3:
        di = 'S'
        
    elif di == 'S' and order ==1:
        di = 'W'
    elif di =='S' and order ==2:
        di = 'N'
    elif di =='S' and order ==3:
        di = 'E'
print(di)