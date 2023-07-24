# sum(buy_list.append(a*b)) 해주게 되면
# buy_list.append(a*b) 이 코드가 by_list에 a*b 값을 추가하면서 리스트 자체를 반환
# type(buy_list.append(a*b))의 타입 = NoneType
x = int(input())
n = int(input())
buy_list = []
for i in range(1, n+1):
    a, b = map(int, input().split())
    buy_list.append(a*b)
if sum(buy_list) ==x:
    print('Yes')
else:
    print('No')