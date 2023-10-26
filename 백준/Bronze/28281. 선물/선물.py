#28281 선물
n, x = map(int,input().split())
price = list(map(int,input().split(' ')))
answer = []
for i in range(len(price)-1):
    answer.append((price[i]*x)+(price[i+1]*x))
print(min(answer))