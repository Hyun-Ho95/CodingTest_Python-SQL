# 2920 음계
scale = {1:'c',
         2:'d',
         3:'e',
         4:'f',
         5:'g',
         6:'a',
         7:'b',
         8:'C'}
num_list = list(map(int,input().split()))
answer = ''
for i in num_list:
    answer += scale[i]

if answer == 'cdefgabC':
    print('ascending')
elif answer == 'Cbagfedc':
    print('descending')
else:
    print('mixed')