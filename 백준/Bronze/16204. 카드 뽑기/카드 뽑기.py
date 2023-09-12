# 16204 카드 뽑기
n, m, k = map(int,input().split())

# 앞,뒷면 모두 O인 카드의 개수
O = min(m,k)
# 앞,뒷면 모두 X인 카드의 개수
X = min(n-m,n-k)

# 모양이 같은 카드의 최대 개수
print(O+X)