###### 24860 Counting Antibodies(항체 수 세기)
vk, jk = map(int,input().split())
vl, jl = map(int,input().split())
vh, dh, jh = map(int,input().split())

# vk*jk => 경쇄 k에 대해서 가변부 v와 j에 대한 가짓수
# vl*jl => 경쇄 l에 대해서 가변부 v와 j에 대한 가짓수
# (vk*jk)+(vl*jl) => 경쇄 k,l에 대한 총 가짓수
# (vh*dh*jh) => 중쇄에 대해서 가변부 v,d,j에 대한 가짓수 (종류1개) 
print(((vk*jk)+(vl*jl))*(vh*dh*jh))