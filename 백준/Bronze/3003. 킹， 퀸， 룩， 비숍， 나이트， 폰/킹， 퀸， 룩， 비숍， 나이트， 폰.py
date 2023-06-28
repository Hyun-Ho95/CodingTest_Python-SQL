# 3003 번 킹, 퀸, 룩, 비숍, 나이트, 폰
# 나는 입력받은 숫자에서 while문으로 숫자를 조정할 생각을 했는데 그러면 
# 얼마나 가감됐는지 알수가 없다

# 따라서, chess 라는 리스트를 만들어서 필요한 개수만큼 미리 할당
# 입력받은 s와의 차이 비교 
chess = [1, 1, 2, 2, 2, 8]
s = list(map(int, input().split()))   
for i in range(len(s)):
    print(chess[i] - s[i], end = ' ')