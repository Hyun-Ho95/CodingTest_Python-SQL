# 26742 Skarpetki(양말)
char = input()
cnt_b = 0
cnt_c = 0
for i in char:
    if i=='B':
        cnt_b += 1
    else:
        cnt_c += 1
print((cnt_b//2)+(cnt_c//2))