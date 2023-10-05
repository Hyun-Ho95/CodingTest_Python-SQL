def solution(code):
    mode = 0
    ret = ''
        
    for idx,k in enumerate(code):
        if mode ==0:
            if k == "1":
                mode = 1
            else:
                if idx % 2 ==0:
                    ret += k  
        else:
            if k =="1":
                mode = 0
            else:
                if idx % 2 !=0:
                    ret += k
    return ret if ret != '' else 'EMPTY'