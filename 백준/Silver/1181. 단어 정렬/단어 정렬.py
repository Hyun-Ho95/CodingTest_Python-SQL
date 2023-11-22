# 1181번 단어 정렬
n = int(input())
answer = []
for _ in range(n):
    word = input()
    answer.append(word)
answer = sorted(set(answer), key = lambda x : (len(x),x))
for char in answer:
    print(char)