# 29823 Pakirobot Manhattanis
coor = [0,0]
n = int(input())
word = input()
for i in word:
    if i =='N':
        coor[1] += 1
    elif i =='E':
        coor[0] += 1
    elif i =='S':
        coor[1] -= 1
    else:
        coor[0] -= 1
print(abs(coor[0])+abs(coor[1]))