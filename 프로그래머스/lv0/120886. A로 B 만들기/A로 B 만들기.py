def solution(before, after):
    for i in before:
        if i in after:
            after = after.replace(i,'',1)
    if after=='':
        return 1
    else:
        return 0