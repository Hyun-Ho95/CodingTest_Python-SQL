def solution(arr):
    answer = 0
    cnt = 0 
    while cnt != len(arr):
        cnt= 0
        before_arr = arr.copy()

        for i in range(len(arr)):
                if arr[i] >= 50 and arr[i]%2==0:
                    arr[i] //=2 # arr[i]를 2로 나눈 후 그 결과를 다시 arr[i]에 할당(소수부분 버리고 정수 부분만 반환)
                elif arr[i] <50 and arr[i]%2!=0:
                    arr[i] = 2*arr[i] + 1

                if arr[i] == before_arr[i]:
                    cnt += 1
        answer += 1
    return answer-1