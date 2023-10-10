def solution(arr):
    i = 0
    stk = []
    while True:
        if i >= len(arr):
            break
        else:
            if stk ==[]:
                stk.append(arr[i])
                i += 1
            elif (stk != []) and (stk[-1] < arr[i]):
                stk.append(arr[i])
                i += 1
            elif (stk != []) and (stk[-1] >= arr[i]):
                stk.remove(stk[-1])
    return stk