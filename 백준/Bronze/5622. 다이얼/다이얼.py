# 5622번 다이얼

# 1. 입력받은 알파벳 -> 숫자 (변환)
# 2. 해당하는 숫자의 다이얼을 돌릴 때 걸리는 시간 계산

# 풀다가 도저히 안 되서 구글링 해보았다. 진짜 똑똑한 사람 많은듯..더 노력하자
# 엄청 어려운 내용은 아니었던 것 같은데 풀지 못해서 아쉬웠다. 조금 더 생각 많이 해보고 유연해지자
dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for j in range(len(word)):
    for i in dial_list:
        if word[j] in i:
            time += dial_list.index(i) + 3
print(time)