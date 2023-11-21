# 2577번 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

answer = a*b*c
array = []

for i in str(answer):
    array.append(i)

for i in range(10):
    if str(i) in array:
        print(array.count(str(i)))
    else:
        print(0)