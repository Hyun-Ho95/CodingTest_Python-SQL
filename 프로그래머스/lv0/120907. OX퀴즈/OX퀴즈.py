def solution(quiz):
    
    ox_result = []
    
    for i in quiz:
        
        start = int(i.split()[0])
        
        if i.split()[1] == '-':
            start -= int(i.split()[2])
            if start == int(i.split()[-1]):
                ox_result.append('O')
            else:
                ox_result.append('X')
        else:
            start += int(i.split()[2])
            if start == int(i.split()[-1]):
                ox_result.append('O')
            else:
                ox_result.append('X')
                
    return ox_result