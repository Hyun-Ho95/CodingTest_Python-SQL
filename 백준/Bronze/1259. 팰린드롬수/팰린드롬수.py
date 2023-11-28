# 1259번 팰린드롬수
while True:
    num = int(input())
    if num ==0:
        break
    else:
        if str(num) == str(num)[::-1]:
            print('yes')
        else:
            print('no')