# 11050 이항계수
n,k = map(int,input().split())
n_fac = 1
k_fac = 1
n_k_fac = 1
for a in range(1,n+1):
    n_fac *= a
    
for b in range(1,k+1):
    k_fac *= b
    
for c in range(1,n-k+1):
    n_k_fac *= c
print(int((n_fac)/(k_fac*n_k_fac)))