def solution(n):
    num_list = []
    for i in range(1,187):
        if i % 3 !=0 and '3' not in str(i):
            num_list.append(i)
    return num_list[n-1]
            