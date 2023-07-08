array = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for i in range(n):
    x, y = list(map(int,input().split()))
    
    for row in range(x, x+10):
        for col in range(y, y+10):
            array[row][col] = '*'

result = 0

for j in array:
    result += j.count('*')
print(result)