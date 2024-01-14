# 1731번 추론(BronzeII)
arr = []
ans_d = []
ans_r = []

for i in range(int(input())):
    arr.append(int(input()))

# 공차수열일 경우
for d in range(0,len(arr)-1):
    ans_d.append(arr[d+1]-arr[d])

# 공비수열일 경우
for r in range(0,len(arr)-1):
    ans_r.append(int(arr[r+1]/arr[r]))

if int(sum(ans_d)/len(ans_d)) == ans_d[0]:
    print(arr[-1] + ans_d[0])
else:
    print(arr[-1] * ans_r[0])