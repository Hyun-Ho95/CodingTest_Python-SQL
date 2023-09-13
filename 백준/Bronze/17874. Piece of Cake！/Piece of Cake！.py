# 17874 Piece of Cake!
n,h,v = map(int,input().split())
print(max((n-h)*v*4,h*v*4,(n-v)*h*4,(n-v)*(n-h)*4))