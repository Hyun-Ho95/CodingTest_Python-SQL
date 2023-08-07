# 6778 Which Alien?
antenna = int(input())
eyes = int(input())


if antenna >= 3 and eyes <= 4:
    print("TroyMartian")
if antenna <= 6 and eyes >= 2:
    print("VladSaturnian")
if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian")

# 여기서 중요한 점은 elif로 하면 두가지 이상의 경우에 해당되는 외계인(ex antenna = 2 , eyes = 3)은 출력되지 않는다
# if를 3줄로 작성해주어야함
