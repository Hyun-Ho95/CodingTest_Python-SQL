# 1673번 치킨 쿠폰
while True:
    try:
        n,k = map(int,input().split())
        chicken = n 
        stamp = n
        service = 0
        
        while stamp // k > 0:
            service += stamp // k
            stamp = (stamp // k) + (stamp % k)
        
        print(chicken + service)
    except EOFError:
        break