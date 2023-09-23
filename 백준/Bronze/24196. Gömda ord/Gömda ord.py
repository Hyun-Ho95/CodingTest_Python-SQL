# 24196 Gömda ord(숨겨진 단어)
s = input()
result = s[0]
alphabet = {chr(i+64): i for i in range(1,27)}
cnt = alphabet[s[0]]
while True:
    if cnt >= len(s):
        break
    else:
        result += s[cnt]
        cnt += alphabet[s[cnt]]
print(result)