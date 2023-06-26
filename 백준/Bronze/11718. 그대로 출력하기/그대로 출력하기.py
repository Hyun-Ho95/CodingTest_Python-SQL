# 11718번 그대로 출력하기
# EOF 처리 방법 숙지
# EOF(End Of File) : 입력 끝남 에러. 데이터가 없어 더이상 값을 읽을 수 없을 떄 발생
while True:
    try:
        print(input())
    except EOFError:
        break