# 1440번 타임머신
time = list(map(int,input().split(':')))
hour = [h for h in range(1,13)]
sec = [s for s in range(60)]

cnt = 0 
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k :
                if time[i] in hour and time[j] in sec and time[k] in sec:
                    cnt += 1
print(cnt)