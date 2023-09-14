# 18414 X に最も近い値 (The Nearest Value)
x, l, r = map(int,input().split())
num_list = [ i for i in range(l,r+1) ]
result = []
for k in num_list:
    result.append(abs(k-x))
print(num_list[result.index(min(result))])