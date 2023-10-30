# 29807 학번을 찾아줘!
array = [0]*5
t = int(input())
sub = list(map(int,input().split()))
for i in range(t):
    array[i] = sub[i]
array
cnt = 0

# 국어-영어
if array[0] > array[2]:
    cnt += (abs(array[0]-array[2]))*508
else:
    cnt += (abs(array[0]-array[2]))*108
    
# 수학-탐구
if array[1]>array[3]:
    cnt += (abs(array[1]-array[3]))*212
else:
    cnt += (abs(array[1]-array[3]))*305
    
# 제2외국어
if array[-1] !=0:
    cnt += array[-1]*707

# 학번
print(cnt*4763)

