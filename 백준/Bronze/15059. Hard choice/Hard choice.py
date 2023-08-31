# 15059 Hard Choice
ca, ba, pa = map(int,input().split())
cr, br, pr = map(int,input().split())
cnt = 0
if ca<cr:
    cnt += cr-ca
if ba<br:
    cnt += br-ba
if pa<pr:
    cnt += pr-pa
print(cnt)