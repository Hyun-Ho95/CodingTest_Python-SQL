# 2566번 최댓값
matrix = []
matrix_m = []
for row in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)
    matrix_m.append(max(row))
    
m = max(matrix_m)

print(m)
print(matrix_m.index(m)+1, matrix[matrix_m.index(m)].index(m)+1)