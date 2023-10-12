def solution(a, b, c, d):
    nums = [a,b,c,d]
    cnts = [nums.count(i) for i in nums]
    if max(cnts) == 4:
        return 1111*a
    elif max(cnts) == 3:
        p = nums[cnts.index(3)]
        q = nums[cnts.index(1)]
        return (10*p +q)**2
    elif max(cnts) == 2:
        if min(cnts) == 2:
            return (a+c)*abs(a-c) if a==b else (a+b)*abs(a-b)
        else:
            p = nums[cnts.index(2)]
            return int((a*b*c*d)/(p**2))
    else:
        return min(nums)