# 1668번 트로피 진열(Bronze II)
arr = []

for _ in range(int(input())):
    arr.append(int(input()))
    
# 왼쪽 방향
max_lh = cnt_l = 0
for i in arr:
    if max_lh < i:
        max_lh = i
        cnt_l += 1

# 오른쪽 방향
max_rh = cnt_r = 0
for j in range(len(arr)-1,-1,-1):
    if max_rh < arr[j]:
        max_rh = arr[j]
        cnt_r += 1
        
print(cnt_l)
print(cnt_r)