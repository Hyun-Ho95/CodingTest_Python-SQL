# 29340 Отряд(분대)
a = input()
b = input()
res = ''
for i in range(len(a)):
    if a[i]>b[i]:
        res += a[i]
    else:
        res += b[i]
print(res)