def solution(my_string):
    
    my_string = my_string.split()
    answer = int(my_string[0])

    for idx, char in enumerate(my_string):
        if char=='+':
            answer += int(my_string[idx+1])
        elif char=='-':
            answer -= int(my_string[idx+1])
    return answer