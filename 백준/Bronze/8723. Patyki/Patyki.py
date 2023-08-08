# 8723 Patyki
lines = list(map(int,input().split()))
lines = sorted(lines)
if lines[0] **2 + lines[1] **2 == lines[2] **2:
    print(1)
elif lines[0]==lines[1]==lines[2]:
    print(2)
else:
    print(0)