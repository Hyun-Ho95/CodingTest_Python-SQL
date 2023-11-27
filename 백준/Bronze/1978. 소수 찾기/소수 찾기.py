# 1978번 소수찾기
n = int(input())
num_list = list(map(int,input().split()))
cnt = 0 

for num in num_list:
    for j in range(2,num+1):
        if num % j ==0:
            if num ==j:
                cnt += 1
            else:
                break
            
print(cnt)