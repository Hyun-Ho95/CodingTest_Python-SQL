# 15051 Máquina de café
a1 = int(input())
a2 = int(input())
a3 = int(input())

sol1 = (a2*2) + (a3*4)
sol2 = (a1*2) + (a3*2)
sol3 = (a1*4) + (a2*2)
print(min(sol1,sol2,sol3))