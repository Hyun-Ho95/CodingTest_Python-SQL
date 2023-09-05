# 15474 鉛筆 (Pencils)
n, a, b, c, d = map(int,input().split())

# X세트 -> a개 * b엔
if n % a !=0:
    x = (n // a +1) * b
else:
    x = (n//a) * b
    
# Y세트 -> c개 * d엔
if n % c !=0:
    y = (n // c +1) * d
else:
    y = (n//c) * d
print(min(x,y))