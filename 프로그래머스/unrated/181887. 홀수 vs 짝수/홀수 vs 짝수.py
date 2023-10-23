def solution(num_list):
    odd = []
    even = []
    for idx,k in enumerate(num_list):
        if idx % 2==0:
            odd.append(k)
        else: even.append(k)            
    return max(sum(odd),sum(even))