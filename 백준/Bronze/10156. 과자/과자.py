# 10156 과자
# k 과자한개 가격
# n 사야하는 과자 수 
# m 현재 가진 돈
k,n,m = map(int,input().split())
if k*n > m:
    print((k*n)-m)
else:
    print(0)