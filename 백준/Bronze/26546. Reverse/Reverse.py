# 26546 Reverse
n = int(input())
for _ in range(n):
    word, a, b = input().split()
    print(word.replace(word[int(a):int(b)],''))