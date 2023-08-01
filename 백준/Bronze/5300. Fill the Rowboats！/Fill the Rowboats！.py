# 5300 Fill the Rowboats!
n = int(input())
result = []

for i in range(1,n+1):
    if i % 6 != 0:
        result.append(str(i))
    else:
        result.append(str(i))
        result.append('Go!')
if result[-1] !='Go!':
    result.append('Go!')
        
print(' '.join(result))