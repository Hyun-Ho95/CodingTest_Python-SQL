# 24083 短針 (Hour Hand)
a = int(input())
b = int(input())
c = a+b
while True:
    if c<=12:
        print(c)
        break
    else:
        c -= 12