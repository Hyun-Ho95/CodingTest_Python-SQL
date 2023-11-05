# 2455번 지능형 기차 
result = []
cnt = 0

for _ in range(4):
    a,b = map(int,input().split())
    result.append(cnt-a)
    cnt -= a
    result.append(cnt+b)
    cnt += b
print(max(result))