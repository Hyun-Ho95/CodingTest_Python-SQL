# 26736 Wynik meczu
char = input()
cnt_a = 0
cnt_b = 0
for i in char:
    if i == 'A':
        cnt_a += 1
    else:
        cnt_b += 1
print(f'{cnt_a} : {cnt_b}')