# 1343번 폴리오미노(SilverV)
poli = input()
poli = poli.replace('XXXX','AAAA')
poli = poli.replace('XX','BB')

if 'X' in poli:
    print(-1)
else: print(poli)