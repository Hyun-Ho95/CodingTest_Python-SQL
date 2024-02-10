# 1543번 문서 검색(SilverV)
doc = input()
word = input()
cnt = 0

while True:
    if word not in doc:
        break
    else:
        if word in doc:
            doc = doc.replace(word,'_',1)
            cnt += 1
print(cnt)