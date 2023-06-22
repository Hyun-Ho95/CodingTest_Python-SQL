alphabet = [chr(i) for i in range(97, 123)]
s = input()

#1 if 문 사용
for i in alphabet:
    if i in s:
        print(s.index(i), end= ' ') # 문자열 s에서 문자열i가 몇번 인덱스에 있냐
    else:
        print(-1, end = ' ')

#2 find 함수 사용
# for i in alphabet:
#     print(s.find(i), end = ' ')