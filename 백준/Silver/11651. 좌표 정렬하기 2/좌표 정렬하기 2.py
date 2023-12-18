# 11651 좌표 정렬하기2 (Silver V)
result = []
for _ in range(int(input())):
    x,y = map(int,input().split())
    result.append([x,y])
result.sort(key=lambda a : (a[1],a[0]))
for i in result:
    print(i[0],i[1])