# 1457번 방 번호(SilverV)
num_list = [0] * 10
n = input()

for idx,k in enumerate(n):
    if int(k)==6 or int(k)==9:
        if num_list[6] <= num_list[9]:
            num_list[6] += 1
        else:
            num_list[9] += 1
    else:
        num_list[int(k)] += 1
print(max(num_list))