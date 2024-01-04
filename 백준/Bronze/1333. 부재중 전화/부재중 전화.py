# 1333번 부재중 전화(Bronze II)
n,l,d = map(int,input().split())
song = [False] * ((n*l)+(n-1)*5) # 앨범 총 길이
len(song)
for i in range(0,len(song),l+5): # 노래 시작시간 
    for j in range(i,i+l): # 노래가 시작되고 재생되는 시간
        song[j] = True

for k in range(0,len(song),d):
    if song[k]==False:
        print(k)
        break
else: print(k+d)