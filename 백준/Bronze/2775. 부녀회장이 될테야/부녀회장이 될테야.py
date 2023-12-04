# 2775번 부녀회장이 될테야
t = int(input())
for _ in range(t):
    floor = int(input())
    num = int(input())
    f0 = [i for i in range(1,num+1)] # 0층 리스트(호 수 길이 만큼의 리스트 생성)
    for k in range(floor): # k(층 수)만큼 반복
        for n in range(1,num):
            f0[n] += f0[n-1]
    print(f0[-1])