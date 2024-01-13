# 1864번 문어 숫자(BronzeII)
word = {'-':0, "\\":1, '(':2, '@':3, '?':4
      , '>':5, '&':6, '%':7, '/': -1}

while True:
    num = input()
    ans = 0
    if num == '#':
        break
    
    for i in range(len(num)):
        ans += word[num[i]] * 8 ** (len(num)-i-1)
    print(ans)
