N = int(input())
group_word = N

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] : # 문자가 연속되면 그냥 다음 반복으로
            continue
        elif word[j] in word[j+1:] : # 다른 문자와 처음 비교될 때 그 이후에도 문자가 나오면 -1
            group_word -= 1          # zzzaaz에서 z와 a 비교하는데 이후 문자열에서 z가 나오므로 -1 하고 두번째 for문 종료
            break                    # 그 이후에 나오지 않는다면 다음 반복으로
print(group_word)