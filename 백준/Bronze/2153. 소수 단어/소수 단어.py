# 2153번 소수 단어(BronzeII)
alphabet_l = {chr(96+i) : i for i in range(1,27)}
alphabet_u = {chr(38+i) : i for i in range(27,53)}

word = input()
cnt = 0

for i in word:
    if i.isupper():
        cnt += alphabet_u[i]
    else:
        cnt += alphabet_l[i]

for i in range(2,cnt+1):
    if cnt % i==0 and i != cnt:
        print('It is not a prime word.')
        break
else: print('It is a prime word.')
        