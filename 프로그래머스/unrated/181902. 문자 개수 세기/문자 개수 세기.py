def solution(my_string):
    result = [0]*52
    
    for i in my_string:
        if i.isupper(): # i가 대문자라면
            result[ord(i)-65] += 1 
        else:
            result[ord(i)-71] += 1
    return result