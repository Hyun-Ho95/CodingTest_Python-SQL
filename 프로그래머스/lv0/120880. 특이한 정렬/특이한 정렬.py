def solution(numlist, n):
    
    n_distance = {}
    
    for idx, k in enumerate(numlist):
        n_distance[idx,abs(k-n)] = k
        
    sorted_n_distance = sorted(n_distance.items(), key=lambda x: (x[0][1],-x[1]))
    result = [value for key,value in sorted_n_distance]
    
    return result