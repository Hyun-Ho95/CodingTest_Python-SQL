# 28113 정보섬의 대중교통
n, a, b = map(int,input().split())
if a > b:
    print('Subway')
elif a == b:
    print('Anything')
else:
    print('Bus')