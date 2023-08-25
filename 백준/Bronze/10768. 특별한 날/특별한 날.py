# 10768 특별한 날
a = int(input())
b = int(input())

if a ==1:
    print('Before')
elif a==2 and b < 18:
    print('Before')
elif a==2 and b==18:
    print('Special')
else:
    print('After')