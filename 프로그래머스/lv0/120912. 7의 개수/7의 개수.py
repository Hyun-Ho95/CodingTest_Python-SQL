def solution(array):
    str_array = [ str(i) for i in array]
    return ''.join(str_array).count('7')
    