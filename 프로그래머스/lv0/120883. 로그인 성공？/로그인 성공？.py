def solution(id_pw, db):
    
    result = []
    
    for d in db:
        if id_pw[0]==d[0] and id_pw[1]==d[1]:
            result.append('login')
        elif id_pw[0]==d[0] and id_pw[1]!=d[1]:
            result.append('wrong pw')
        elif id_pw[0]!=d[0] and id_pw[1]!=d[1]:
            result.append('fail')
    
    if 'login' in result:
        return 'login'
    elif 'wrong pw' in result:
        return 'wrong pw'
    else:
        return 'fail'