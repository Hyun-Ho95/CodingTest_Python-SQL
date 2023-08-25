# 9782 Median 
n=1

while True:
    d = list(map(int, input().split()))
    num = d[0]
    num_list = d[1:]
    if num ==0:
        break
    else:
        if num % 2 !=0:
            print(f'Case {n}: {num_list[int((num+1)/2)-1]:.1f}')
            n += 1
        else:
            print(f'Case {n}: {(num_list[int(num/2)]+num_list[int(num/2)-1])/2}')
            n += 1