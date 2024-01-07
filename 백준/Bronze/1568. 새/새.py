# 1568번 새(BronzeII)
birds = int(input())
num = 1
sec = 0
while True:
    if birds ==0:
        break
    
    birds -= num
    sec += 1
    num += 1
    if birds < num:
        num = 1
print(sec)