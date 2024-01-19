# 1975번 Number Game(BronzeII)
import sys 
t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    
    for i in range(2,n+1):
        x = n
        while True:
            if x%i ==0:
                cnt += 1
                x //= i
            else:
                break
    print(cnt)
        