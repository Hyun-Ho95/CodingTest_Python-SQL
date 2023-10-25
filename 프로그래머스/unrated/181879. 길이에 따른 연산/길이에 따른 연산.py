def solution(num_list):
    if len(num_list)>=11:
        ans1 = 0
        for i in num_list:
            ans1 += i
        return ans1
    else:
        ans2 = 1
        for j in num_list:
            ans2 *= j
        return ans2