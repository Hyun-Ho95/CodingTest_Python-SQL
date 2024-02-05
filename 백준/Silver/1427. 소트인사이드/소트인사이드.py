# 1427번 소트 인사이드(SilverV)
num = list(map(int,input()))
num = sorted(num,reverse=True)
print(''.join(map(str,num)))