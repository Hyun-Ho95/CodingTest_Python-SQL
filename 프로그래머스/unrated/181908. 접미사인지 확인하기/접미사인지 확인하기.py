def solution(my_string, is_suffix):
    result = []
    for i in range(len(my_string)):
        result.append(my_string[i:])
    return 1 if is_suffix in result else 0