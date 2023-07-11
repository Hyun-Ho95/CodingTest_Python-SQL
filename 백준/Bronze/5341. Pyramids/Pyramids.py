#### 5341번 Pyramids

while True:
    n = int(input())
    cnt = 0
    
    if n ==0:
        break
    else:
        for i in range(n,0,-1):
            cnt += i
        print(cnt)