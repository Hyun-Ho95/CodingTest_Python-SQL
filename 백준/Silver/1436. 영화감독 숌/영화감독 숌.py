#1436번 영화감독 숌(Silver V)
num = int(input())
end = 665
cnt = 0 
while True:
    # 종말의 수(end) 665부터 시작
    end += 1
    
    if str(end).count('666') >= 1:
        cnt += 1
        
        # 시리즈 수(cnt)와 입력값(n)이 같다면 그때의 종말의 수(end)출력하고 break로 탈출
        if cnt == num:
            print(end)
            break