# 2744번 대소문자 바꾸기
word = input()

for i in word:
    if i == i.upper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')