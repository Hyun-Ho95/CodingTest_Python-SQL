# 25991 Lots of Liquid
n = int(input())
cnt = 0
num_list = list(input().split())

for i in num_list:
    cnt += float(i)**3
print(cnt ** (1/3))