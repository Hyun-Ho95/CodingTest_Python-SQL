# 2490번 윷놀이(Bronze III)
import sys
for _ in range(3):
    yut = list(map(int,input().split()))
    
    #모 
    if yut.count(1) == 4:
        print('E')
    
    #윷
    elif yut.count(0) == 4:
        print('D')
    
    #걸
    elif yut.count(0) == 3:
        print('C')
    
    #개
    elif yut.count(1) == 2:
        print('B')
        
    #도
    elif yut.count(0) == 1:
        print('A')