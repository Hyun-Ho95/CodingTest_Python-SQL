# 6888 Terms of Office
x = int(input())
y = int(input())

start_num = 60
print('All positions change in year', x)

while True:
    if x + start_num <= y:
        print('All positions change in year', x+start_num)
        start_num += 60
    else:
        break
