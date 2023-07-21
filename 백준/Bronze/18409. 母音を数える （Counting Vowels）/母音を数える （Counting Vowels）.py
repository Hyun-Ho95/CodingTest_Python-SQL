# 18409 母音を数える (Counting Vowels)
n = int(input())
word = input()

vowel = list('aeiou')
cnt = 0

for s in word:
    if s in vowel:
        cnt += 1
print(cnt)