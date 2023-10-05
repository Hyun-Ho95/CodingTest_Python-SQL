def solution(a, d, included):
    sequence = []
    cnt = 0
    
    for _ in range(len(included)):
        sequence.append(a)
        a += d
    for idx,k in enumerate(included):
        if  k == True:
            cnt += sequence[idx]
    return cnt