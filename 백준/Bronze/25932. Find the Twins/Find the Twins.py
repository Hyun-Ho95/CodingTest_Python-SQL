# 25932 Find the Twins
n = int(input())
for _ in range(n):
    jersey_numbers = list(input().split())
    if '17' in jersey_numbers and '18' not in jersey_numbers:
        print(' '.join(jersey_numbers))
        print('zack')
        print('')
    elif '17' not in jersey_numbers and '18' in jersey_numbers:
        print(' '.join(jersey_numbers))
        print('mack')
        print('')
    elif '17' not in jersey_numbers and '18' not in jersey_numbers:
        print(' '.join(jersey_numbers))
        print('none')
        print('')
    elif '17' in jersey_numbers and '18' in jersey_numbers:
        print(' '.join(jersey_numbers))
        print('both')
        print('')