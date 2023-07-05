# 2738번 행렬 덧셈
n, m = map(int, input().split())

matrix_a = []
matrix_b = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix_a.append(row)
    
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_b.append(row)
    
for row in range(n):
    for col in range(m):
        print(matrix_a[row][col] + matrix_b[row][col], end=' ')
    print()