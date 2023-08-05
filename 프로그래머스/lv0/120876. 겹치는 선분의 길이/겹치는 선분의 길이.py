def solution(lines):
    
    num_list = [k for i in lines for k in range(i[0],i[1])]
    result = [ j for j in num_list if num_list.count(j)>=2 ]
    
    return len(set(result))