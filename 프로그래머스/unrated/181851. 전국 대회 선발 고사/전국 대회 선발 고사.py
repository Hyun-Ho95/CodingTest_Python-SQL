def solution(rank, attendance):
    arr = []
    possible = []
    answer = []
    
    for idx,k in enumerate(attendance):
        if k == True:
            arr.append(idx)
    for i in arr:
        possible.append(rank[i])
    final = sorted(possible)[:3]
    
    for j in final:
        answer.append(rank.index(j))
    
    return 10000*answer[0] + 100*answer[1] + answer[2]