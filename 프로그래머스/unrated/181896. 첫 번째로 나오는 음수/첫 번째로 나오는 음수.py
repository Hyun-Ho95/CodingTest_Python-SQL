def solution(num_list):
    for idx,k in enumerate(num_list):
        if k<0:
            return idx
    return -1