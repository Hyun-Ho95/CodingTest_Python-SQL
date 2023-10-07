def solution(arr, queries):
    result = []
    for i in queries:
        num_list = []
        for j in range(i[0],i[1]+1):
            if arr[j] > i[-1]:
                num_list.append(arr[j])
        if num_list == []:
            num_list.append(-1)
        result.append(min(num_list))
    return result