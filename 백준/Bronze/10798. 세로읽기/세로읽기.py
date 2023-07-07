# 10798번 세로읽기
words = [input() for i in range(5)]

# words[i][j] 할 때 words[0][0], words[1][0], words[2][0]...으로 간다는 걸 생각하고 풀자
for j in range(15): # 문자열 최대길이 (15)
    for i in range(5):
        if j < len(words[i]): # 예를 들어 ,문자열 길이(=j) 4일 때, len(words[i])=4라면 
                              # 해당 문자열의 words[i][j]는 출력하지 않음
            print(words[i][j], end="")