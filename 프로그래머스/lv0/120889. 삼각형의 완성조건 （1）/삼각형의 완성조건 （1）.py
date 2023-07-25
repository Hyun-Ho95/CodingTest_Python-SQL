def solution(sides):
    
    other_sides = sides.copy()
    other_sides.remove(max(sides))
    
    if max(sides) < sum(other_sides):
        return 1
    else:
        return 2