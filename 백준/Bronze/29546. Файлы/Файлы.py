# 29546 Файлы
pic_dic = {1 : 'idx1001.jpg'
          ,2 : 'idx1000.jpg'
          ,3 : 'idx1014.jpg'}
n = int(input())
pic_list = []
for _ in range(n):
    pic = input()
    pic_list.append(pic)
    
m = int(input())
answer = []
for _ in range(m):
    l, r = map(int,input().split())
    for i in range(l-1,r):
        print(pic_list[i])
