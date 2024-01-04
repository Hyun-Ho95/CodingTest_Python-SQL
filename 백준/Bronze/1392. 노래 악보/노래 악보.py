# 1392번 노래 악보(BronzeII)
n,q = map(int, input().split())

bi = []
for i in range(n):
    s = int(input())
    bi.extend([i+1] * s)

for j in range(q):
    t = int(input())
    print(bi[t])