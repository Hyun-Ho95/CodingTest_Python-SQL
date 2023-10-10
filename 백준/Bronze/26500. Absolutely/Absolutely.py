# 26500 Absolutely
n = int(input())

for _ in range(n):
    a, b = map(float,input().split())
    print(round(abs(b-a),1))