# 28431 양말 짝 찾기
num_list = []
cnt = 0

for _ in range(5):
    num = int(input())
    if num in num_list:
        cnt -= num
        num_list.remove(num)
    else:
        cnt += num
        num_list.append(num)
print(cnt)