# 9772 Quadrants
while True:
    a, b = map(float,input().split())
    if a==0 and b==0:
        print('AXIS')
        break
    else:
        if a>0 and b>0:
            print('Q1')
        elif a>0 and b<0:
            print('Q4')
        elif a<0 and b>0:
            print('Q2')
        elif a<0 and b<0:
            print('Q3')
        elif (a==0 and b>0) or (a==0 and b<0) or (a<0 and b==0) or (a>0 and b==0):
            print('AXIS')
            