# 26489 Gum Gum for Jay Jay
cnt = 0
while True:
    try:
        word = list(input().split())
        cnt += 1
    except EOFError:
        break
print(cnt)