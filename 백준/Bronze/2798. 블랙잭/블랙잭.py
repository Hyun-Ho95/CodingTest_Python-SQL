# 2798번 블랙잭
n,m = map(int,input().split())
num_list = list(map(int,input().split()))
result = []
for i in num_list[:-2]:
    for j in num_list[1:-1]:
        for k in num_list[2:]:
            if i+j+k <= m and (i!=j and j!=k and i!=k):
                result.append(i+j+k)
print(max(set(result)))