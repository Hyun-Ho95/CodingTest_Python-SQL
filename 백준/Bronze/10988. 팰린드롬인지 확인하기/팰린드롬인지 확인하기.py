# 10988번 팰린드롬인지 확인하기
word = input()
if word == word[::-1]:
    print(int(1))
else:
    print(int(0))