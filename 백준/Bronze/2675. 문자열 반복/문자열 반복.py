t = int(input())

for _ in range(t):
    r,s = input().split()
    for i in range(len(s)):
        print(s[i] * int(r), end='')
    print() # 각 테스트 케이스 별로 개행. 이렇게 하지 않으면 "5 /HTP"가 첫번째값 뒤에 붙어서 나옴