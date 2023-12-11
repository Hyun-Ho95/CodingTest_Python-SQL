# 7568번 덩치 
n = int(input())
body = []
for _ in range(n):
    x,y = map(int,input().split())
    body.append([x,y])

result = []
for i in body:
    rank = 1
    new_body = list(filter(lambda x : x !=i,body))
    for j in new_body:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    result.append(str(rank))
print(' '.join(result))
        