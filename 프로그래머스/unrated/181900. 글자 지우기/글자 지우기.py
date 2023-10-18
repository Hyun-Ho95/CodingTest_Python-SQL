def solution(my_string, indices):
    result = ''
    for idx,k in enumerate(my_string):
        if idx not in indices:
            result += k
    return result