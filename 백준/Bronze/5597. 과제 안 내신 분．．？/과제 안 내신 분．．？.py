# 숫자를 한번에 입력받는게 아니라 1줄에 있는 숫자 1개씩 입력받는 걸 숙지!
num_list = [ n for n in range(1,31) ]
for _ in range(28):
    data = int(input()) # 예제에 있는 1부터 30사이 랜덤한 숫자를 28번 넣어줌
    num_list.remove(data) # 1부터 30까지있는 출석부(num_list)에서 과제 제출하지 않은 사람만 남기기
print(min(num_list))
print(max(num_list))