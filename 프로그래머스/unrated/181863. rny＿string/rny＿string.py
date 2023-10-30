def solution(rny_string):
    result = ''
    for i in rny_string:
        if i != 'm':
            result += i
        else:
            result += 'rn'
    return result