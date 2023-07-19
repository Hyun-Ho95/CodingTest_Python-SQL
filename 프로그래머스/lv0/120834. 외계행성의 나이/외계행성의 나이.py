def solution(age):
    age = str(age)
    result = ''
    
    age_list = {0:'a', 1:'b', 2:'c', 
              3:'d', 4:'e', 5:'f',
              6 :'g', 7 :'h', 8:'i',
              9:'j'}
    
    for idx, k in enumerate(age):
        result += age_list[int(k)]
    return result