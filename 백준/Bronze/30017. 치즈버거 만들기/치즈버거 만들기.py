# 30017 치즈버거 만들기
a,b = map(int,input().split())
if a > b:
    print(b+(b+1))
elif a==b:
    print(a+(b-1))
else:
    print(a+(a-1))
    