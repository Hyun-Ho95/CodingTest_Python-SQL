# 20233 Bicycle(자전거)
a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
if t<=30:
    a_fee = a
    b_fee = b 
elif t>30 and t<45:
    a_fee = a + (t-30)*x*21
    b_fee = b
elif t>=45:
    a_fee = a + (t-30)*x*21
    b_fee = b + (t-45)*y*21
print(a_fee,b_fee)