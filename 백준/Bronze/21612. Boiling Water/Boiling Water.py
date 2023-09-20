# 21612 Boiling Water(끓는 물)
# 해수면보다 낮을 때 -> 기압 증가, 끓는 점 증가
# 해수면보다 높을 때 -> 기압 감소, 끓는 점 감소
b = int(input())
p = 5*b-400
print(p)
if p <100:
    print(1)
elif p >100:
    print(-1)
else:
    print(0)