# 1225번 이상한 곱셈 (Bronze II)
a,b = input().split()
arr = []
for i in range(len(a)):
    arr.append(int(a[i]))

ans = sum(arr)
cnt = 0

for j in range(len(b)):
    cnt += ans*int(b[j])
print(cnt)