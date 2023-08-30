# 13866 팀 나누기 
level = list(map(int,input().split()))
x = max(level)
y = min(level)

level.remove(max(level))
level.remove(min(level))
print(abs(sum(level) - (x + y)))