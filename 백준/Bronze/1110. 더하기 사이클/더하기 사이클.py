# 1110번 더하기 사이클(BronzeI)
n = input()
if int(n) < 10:
    n = '0' + str(n)
copy = n
cnt = 0
ans = 0

while True:
    if len(str(int(copy[0]) + int(copy[1]))) >=2:
        cnt = copy[1] + str(int(copy[0]) + int(copy[1]))[1]
        ans += 1
        copy = cnt
        
    else:
        cnt = copy[1] + str(int(copy[0]) + int(copy[1]))
        ans += 1
        copy = cnt
        
    if cnt == n:
        break
print(ans)