# 24087 アイスクリーム (Ice Cream)
s = int(input())
a = int(input())
b = int(input())

cnt = 250
while True:
    if a >= s:
        print(cnt)
        break
    else:
        a += b
        cnt += 100