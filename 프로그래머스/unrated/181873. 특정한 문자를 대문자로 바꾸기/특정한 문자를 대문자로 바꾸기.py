def solution(my_string, alp):
    my_string = list(my_string)
    for idx,k in enumerate(my_string):
        if k==alp:
            my_string[idx] = k.upper()
    return ''.join(my_string)