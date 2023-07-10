# 2475번 검증수
uniq_num = list(map(int,input().split()))
uniq_num_list = []

for i in uniq_num:
    uniq_num_list.append(i**2)
print(sum(uniq_num_list)%10)