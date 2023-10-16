def solution(my_string, m, c):
    cnt = c
    result = ''
    while True:
        if cnt > len(my_string):
            break
        else:
            result += my_string[cnt-1]
            cnt += m
    return result