# 5357 Dedupe
n = int(input())
for i in range(n):
    word = input()
    result = word[0]
    for i in range(1,len(word)):
        if word[i] != result[-1]:
            result += word[i]
        else:
            continue
    print(result)