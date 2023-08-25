# 10797 10부제
cnt = 0
n = int(input())
car_list = list(map(int,input().split()))

for i in car_list:
    if i == n:
        cnt +=1
print(cnt)