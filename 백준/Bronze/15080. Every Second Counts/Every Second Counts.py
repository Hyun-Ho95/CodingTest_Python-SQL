# 15080 Every Second Counts (매 초가 중요해)
h1,m1,s1 = map(int,input().split(':'))
h2,m2,s2= map(int,input().split(':'))
t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2
if (t2-t1)<0 :
    print((t2-t1)+(3600*24))
else:
    print(t2-t1)