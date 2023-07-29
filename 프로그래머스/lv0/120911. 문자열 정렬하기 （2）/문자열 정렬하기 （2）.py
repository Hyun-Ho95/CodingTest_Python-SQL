def solution(my_string):
    new_string = ''
    for i in my_string:
        new_string += i.lower()
    return ''.join(sorted((new_string)))