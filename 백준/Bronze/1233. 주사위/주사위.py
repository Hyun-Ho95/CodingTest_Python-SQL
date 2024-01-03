# 1233번 주사위(Bronze II)
from collections import Counter
s1, s2, s3 = map(int,input().split())
ans = []
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            ans.append(i+j+k)
print(Counter(ans).most_common()[0][0])
