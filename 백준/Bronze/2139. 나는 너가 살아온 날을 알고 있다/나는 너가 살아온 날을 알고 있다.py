# 2139번 나는 너가 살아온 날을 알고 있다(BronzeII)
while True:
    d, m, y = map(int,input().split())
    cnt = 0 
    if d==0 and m==0 and y==0:
        break
    else:
        if (y%4==0 and y%100!=0) or y%400 ==0: #윤년
            dic = {1:31,2:29,3:31,4:30
                  ,5:31,6:30,7:31,8:31
                  ,9:30,10:31,11:30,12:31}
            arr = [i for i in range(1,m+1)]
            for j in range(1,len(arr)):
                cnt += dic[j]
            cnt += d
            print(cnt)
        else:
            dic = {1:31,2:28,3:31,4:30
                  ,5:31,6:30,7:31,8:31
                  ,9:30,10:31,11:30,12:31}
            arr = [i for i in range(1,m+1)]
            for j in range(1,len(arr)):
                cnt += dic[j]
            cnt += d
            print(cnt)