# 1251번 단어 나누기(Silver V)
word = input()
ans = []

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        ans.append(a+b+c)
print(sorted(ans)[0])