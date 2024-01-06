# 1408번 24(BronzeII)
h1,m1,s1 = list(map(int,input().split(':')))
h2,m2,s2 = list(map(int,input().split(':')))

# 임무 시작 시각 - 현재 시각
total = (h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1)

# 현재 시각이 임무 시각보다 뒤에 있다면 24시간 더해주기
if total < 0:
    total += 3600*24
    
total
x,y,z = (total // 3600) , (total % 3600) // 60 , (total % 60)
print('%02d:%02d:%02d' % (x,y,z))