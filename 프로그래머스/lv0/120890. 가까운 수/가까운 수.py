def solution(array, n):
    
    new_array = []
    array.sort()

    for num in array:
        new_array.append(abs(num-n))

    answer = array[new_array.index(min(new_array))]
    return answer