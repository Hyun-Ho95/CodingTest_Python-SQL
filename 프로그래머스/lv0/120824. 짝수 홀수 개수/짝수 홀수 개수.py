def solution(num_list):
    odd = []
    even = []
    
    for i in num_list:
        if i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)
    result = [len(even), len(odd)]
    return result