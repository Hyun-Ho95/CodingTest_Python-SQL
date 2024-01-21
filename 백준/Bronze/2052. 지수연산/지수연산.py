# 2052번 지수연산(BronzeII)
n = int(input())
n = "%.250f" % (1/(2**n))
print(n.rstrip('0'))