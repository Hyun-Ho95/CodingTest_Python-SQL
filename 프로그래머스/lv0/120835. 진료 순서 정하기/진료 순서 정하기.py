def solution(emergency):
    
    sort_emergency = sorted(emergency, reverse=True)
    order = []
    
    for i in emergency:
        order.append(sort_emergency.index(i)+1)
    return order