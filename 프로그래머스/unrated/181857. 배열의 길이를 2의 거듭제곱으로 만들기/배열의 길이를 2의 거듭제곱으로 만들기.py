def solution(arr):
    max_len = [1,2,4,8,16,32,64,128,256,512,1024]
    answer = []
    if len(arr) in max_len:
        return arr
    else:
        for i in max_len:
            if i >= len(arr):
                answer.append(i-len(arr))
        min_ans = min(answer)
        for _ in range(min_ans):
            arr.append(0)
        return arr