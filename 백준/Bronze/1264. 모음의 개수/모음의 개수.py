# 1264 모음의 개수
vowel = ['a','e','i','o','u', 'A','E','I','O','U']

while True:
    word = list(input())
    cnt = 0
    if '#' in word:
        break
    else:
        for i in word:
            if i in vowel:
                cnt += 1
        print(cnt)        