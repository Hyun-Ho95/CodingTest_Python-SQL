# 18698 The Walking Adam
t = int(input())
for _ in range(t):
    walk = input()
    if 'D' in walk:
        print(walk.index('D'))
    else:
        print(len(walk))