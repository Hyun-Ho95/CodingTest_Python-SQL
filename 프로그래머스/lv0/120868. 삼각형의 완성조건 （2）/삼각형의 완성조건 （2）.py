def solution(sides):
    # sides = [11,7]을 예로 들 때
    
    # 1) 나머지 한 변이 가장 긴 변인 경우

    # 두변의 합 18보다는 작고 11보다는 큰 변의 개수
    # 11 < x < 18 -> 양쪽 다 등호가 없는 경우에 x 개수를 구하려면 (큰수-작은수-1)
    # sum(sides)-max(sides)-1

    # 2) 둘 중에 한 변이 가장 긴 변인 경우

    # 두변의 차 4보다 크고 11보다 작거나 같은 변의 개수
    # 4 < x <= 11 -> 한쪽에만 등호가 있는 경우엔 (큰 수 - 작은 수)
    # max(sidees)-(max(sides)-min(sides))

    # 3) 두 가지 경우의 수를 더하기
    # (sum(sides)-max(sides)-1) + (max(sides)-max(sides)+min(sides))
    return sum(sides) - max(sides) + min(sides) -1