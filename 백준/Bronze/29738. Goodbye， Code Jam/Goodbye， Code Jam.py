# 29738 Goodbye, Code Jam
t = int(input())
for i in range(1,t+1):
    n = int(input())
    if n <= 25:
        print(f'Case #{i}: World Finals')
    elif n <= 1000:
        print(f'Case #{i}: Round 3')  
    elif n <= 4500:
        print(f'Case #{i}: Round 2')
    else:
        print(f'Case #{i}: Round 1')