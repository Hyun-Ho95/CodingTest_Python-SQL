# 10816번 숫자 카드 (Silver V)
n = int(input())
num_list = set(map(int,input().split()))

m = int(input())
find_num = list(map(int,input().split()))

result = []
for i in find_num:
    if i in num_list:
        result.append(1)
    else:
        result.append(0)
print(' '.join(map(str,result)))