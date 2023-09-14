# 18330 Petrol(휘발유)
n = int(input())
k = int(input())
if n >= (60+k):
    print((60+k)*1500 + (n-60-k)*3000)
else:
    print(n*1500)