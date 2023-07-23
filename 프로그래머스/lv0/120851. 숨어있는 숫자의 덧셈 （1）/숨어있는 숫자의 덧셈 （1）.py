def solution(my_string):
    
    num_list = []
    
    for i in my_string:
        if i.isdigit():
            num_list.append(int(i))
    return sum(num_list)