# 26766 Робинзон Крузо(로빈슨 크루소)
n = int(input())
if n < 4:
    print('I'*n)
elif n % 5==0:
    print('V' * (n //5))
else:
    print( 'V' * (n // 5) + 'I' * (n % 5) )