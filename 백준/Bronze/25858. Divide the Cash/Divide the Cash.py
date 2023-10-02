# 25858 Divide the Cash (상금 분배)
n, d = map(int,input().split())
solved = [ int(input()) for _ in range(n) ]

for i in range(n):
    print(int((d/sum(solved))*solved[i]))