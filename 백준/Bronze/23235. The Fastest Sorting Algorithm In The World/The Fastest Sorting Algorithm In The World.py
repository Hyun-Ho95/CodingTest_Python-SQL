# 23235 The Fastest Sorting Algorithm In The World
cnt = 0
while True:
        num_list = list(map(int,input().split()))
    
        if 0 in num_list:
            break
        else:
            sorted(num_list)
            cnt += 1
            print(f'Case {cnt}: Sorting... done!')