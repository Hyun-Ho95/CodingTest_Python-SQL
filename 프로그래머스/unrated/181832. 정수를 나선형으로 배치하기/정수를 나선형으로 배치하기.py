def solution(n):
    # 배열 생성
    array = [[0 for _ in range(n)]for _ in range(n)]

    # 시작좌표/방향
    # 시계방향으로 돌으므로 처음엔 오른쪽
    x, y = 0,0
    direc = 'r'

    # 3. n * n 만큼 반복(이동)
    for i in range(1,n**2+1):

        # 4. 시작값 1로 설정
        array[x][y] = i

        # 5. 진행방향 오른쪽일 때
        if direc == 'r':
            # 5-1) 인덱스를 벗어나거나  / 5-2) 진행방향에 값이 있을 때 
            if y + 1 == n or array[x][y+1] !=0:
                # 5-3 아래방향으로 전환
                direc = 'd'
                # 5-4 다음 행으로 넘어가기 위해서 x += 1
                x += 1
            else:
                # 5-5 오른쪽 칸으로 계속 움직이기
                y += 1

        # 6. 진행방향 아래쪽일 때
        elif direc == 'd':
            # 6-1) 인덱스를 벗어나거나  / 6-2) 진행방향에 값이 있을 때 
            if x + 1 == n or array[x+1][y] !=0:
                # 6-3 왼쪽방향으로 전환
                direc = 'l'
                # 6-4 이전 열로 넘어가기 위해서 y -= 1
                y -= 1
            else:
                # 6-5 아래칸으로 계속 움직이기
                x += 1

        # 7. 진행방향 왼쪽일 때
        elif direc == 'l':
            # 7-1 진행방향에 값이 있을 때 
            #      (인덱스의[-1]로 가게되면 이미 값이 있는 경우와 똑같기 때문에 따로 적지 않는다)
            if array[x][y-1] !=0:
                # 7-2 위쪽방향으로 전환
                direc = 'u'
                # 7-3 이전 행으로 넘어가기 위해서 x -= 1
                x -= 1
            else:
                # 7-4 왼쪽칸으로 계속 움직이기
                y -= 1

        # 8. 진행방향 위쪽일 때
        elif direc == 'u':
            # 8-1 진행방향에 값이 있을 때 
            #      (인덱스의[-1]로 가게되면 이미 값이 있는 경우와 똑같기 때문에 따로 적지 않는다)
            if array[x-1][y] !=0:
                # 8-2 오른쪽방향으로 전환
                direc = 'r'
                # 8-3 다음 열로 넘어가기 위해서 y += 1
                y += 1
            else:
                # 7-4 위칸으로 계속 움직이기
                x -= 1
    return array