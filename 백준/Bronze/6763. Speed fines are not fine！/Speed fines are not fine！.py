# 6763 Speed fines are not fine!
limit_speed = int(input())
car_speed = int(input())

if limit_speed >= car_speed:
    print('Congratulations, you are within the speed limit!')
elif limit_speed + 1 <= car_speed <= limit_speed + 20:
    print('You are speeding and your fine is ${}.'.format(100))
elif limit_speed + 21 <= car_speed <= limit_speed + 30:
    print('You are speeding and your fine is ${}.'.format(270))
elif limit_speed + 31 <= car_speed:
    print('You are speeding and your fine is ${}.'.format(500))