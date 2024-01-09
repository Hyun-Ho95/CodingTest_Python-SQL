# 1673번 치킨 쿠폰
while True:
    try:
        n,k = map(int,input().split())
        chicken = n
        stamp = n
        
        while True:
            if stamp//k==0:
                break
            
            chicken += stamp // k
            stamp = stamp // k + stamp %k
        
        print(chicken)
    except EOFError:
        break