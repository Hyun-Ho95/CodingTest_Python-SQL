def solution(str_list):
    for idx,k in enumerate(str_list):
        if k == 'l':
            return str_list[:idx]
        elif k == 'r':
            return str_list[idx+1:]
    return []