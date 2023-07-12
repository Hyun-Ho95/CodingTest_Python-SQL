def solution(n):
    cnt = 1
    while True:
        if (6 * cnt) % n ==0:
            return cnt
            break
        else:
            cnt += 1
            continue
        