# 1434번 책 정리(BronzeII)
n,m = map(int,input().split())
box = list(map(int,input().split()))
book = list(map(int,input().split()))

for i in range(len(book)):
    for j in range(len(box)):
        if book[i] > box[j]:
            continue #현재 박스 테이프로 봉인하고 치우는 역할
        box[j] -= book[i]
        break
print(sum(box))