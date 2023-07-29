# 2845 파티가 끝나고 난 뒤
l, p  = map(int,input().split())
people = list(map(int,input().split()))
answer = [ str(i-(l*p)) for i in people]
print(' '.join(answer))