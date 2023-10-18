# 27182 Rain Diary
n,m = map(int,input().split())
if n >= 8:
    print(n-7)
else:
    x = 14+m-n
    print(x-(7-n))