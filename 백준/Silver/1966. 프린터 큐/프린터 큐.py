# 1966번 프린터큐(Silver III)
import sys
# 테스트 케이스 개수
t = int(input())

for _ in range(t):
    # m: 문서의 개수
    # n: 몇번째로 출력되는지 알고 싶은 숫자의 현재 위치
    n,m = map(int,input().split())
    
    # 문서들 간 우선 순위
    priority = list(map(int,input().split()))

    # 문서의 기존 위치(인덱스) 저장
    # 인쇄되면서 길이와 순서가 점점 변하므로
    index = [i for i in range(n)]
    
    # 몇번째에 출력이 되는지 카운트
    cnt = 0
    
    while True:
        # 제일 처음 있는 문서가 중요도가 제일 높다면
        if priority[0] == max(priority):
            # 그 문서는 바로 인쇄 (인쇄횟수 +1)
            cnt += 1

            # 만약 찾고 싶었던 문서였다면 몇번째에 인쇄된건지 인쇄횟수 출력
            if index[0] == m:
                print(cnt)
                break
            # 찾고 싶었던 문서가 아니라면  
            else:
                del priority[0]
                del index[0]

        # 다른 문서의 우선순위가 높다면
        else:
            # 해당문서는 인쇄되지 않고 인덱스와 중요도가 후순위로 밀림
            priority.append(priority[0])
            del priority[0]

            index.append(index[0])
            del index[0]