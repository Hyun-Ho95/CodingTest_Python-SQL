# 1439번 뒤집기(SilverV)
s = input()
cnt = 0
zero = list(filter(None,s.split('0')))
one = list(filter(None,s.split('1')))

if s.count('0') == len(s) or s.count('1') == len(s):
    print(0)
elif len(one) >= len(zero):
    cnt += len(zero)
    print(cnt)
elif len(zero) >= len(one):
    cnt += len(one)
    print(cnt)