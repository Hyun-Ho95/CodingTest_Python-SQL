# 1977번 완전제곱수(BronzeII)
import math
m = int(input())
n = int(input())
ans = []

for i in range(m,n+1):
    if len(str(math.sqrt(i))) <= 5:
        ans.append(i)
if ans == [] :
    print(-1)
else:
    print(sum(ans))
    print(min(ans))