# 8710 - Koszykarz
k, w, m = map(int,input().split()) 
cnt = 0
if (w-k)%m != 0:
    cnt += 1
print((w-k)//m + cnt)