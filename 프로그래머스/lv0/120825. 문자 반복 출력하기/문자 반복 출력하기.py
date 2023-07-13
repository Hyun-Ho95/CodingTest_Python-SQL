def solution(my_string, n):
    
    iter_word = ''
    
    for i in range(len(my_string)):
        iter_word = iter_word + (my_string[i]*n)
        
    return iter_word