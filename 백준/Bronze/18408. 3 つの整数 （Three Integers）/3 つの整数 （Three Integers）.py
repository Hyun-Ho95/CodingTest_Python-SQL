num_list = list(map(int,input().split()))
cnt1 = 0
cnt2 = 0
num_list
for i in num_list:
    if i==1:
        cnt1 += 1
    else:
        cnt2 += 1
if max(cnt1,cnt2) == cnt1:
    print(1)
else:
    print(2)