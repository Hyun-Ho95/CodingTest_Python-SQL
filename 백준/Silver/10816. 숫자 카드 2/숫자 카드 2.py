# 10816번 숫자 카드2 (Silver IV)
n = int(input())
num_list = list(map(int,input().split()))

num_dic = {}
for _ in range(len(num_list)):
    if len(num_list) >=0:
        if num_list[-1] in num_dic.keys():
            num_dic[num_list.pop()] += 1
        else:
            num_dic[num_list.pop()] = 1
            
m = int(input())
find_num = list(map(int,input().split()))

for i in find_num:
    if i in num_dic.keys():
        print(num_dic[i], end = ' ')
    else:
        print(0, end = ' ')