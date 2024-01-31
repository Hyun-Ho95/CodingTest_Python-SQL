# 1380번 귀걸이(SilverV)
scenario = 1
while True:
    n = int(input())
    if n==0:
        break
    
    ans = 0 
    girls = []
    for _ in range(n):
        girls.append(input())
    
    num_list = []
    for _ in range(2*n-1):
        num,alphabet = input().split()
        num_list.append(num)
    
    for i in num_list:
        if num_list.count(i) ==1:
            ans = int(i)
            break
    print(scenario,girls[ans-1])
    scenario += 1