# 17362 수학은 체육과목 입니다2
# 다섯손가락이라 %5를 생각했는데 규칙이 발견되지 않음
# 끝손가락들(엄지,새끼)의 주기인 %8을 하게되면 규칙이 생김
n = int(input())
if n%8 ==1:
    print(1)
elif n%8 in [0,2]:
    print(2)
elif n%8 in [3,7]:
    print(3)
elif n%8 in [4,6]:
    print(4)
elif n%8 ==5:
    print(5)