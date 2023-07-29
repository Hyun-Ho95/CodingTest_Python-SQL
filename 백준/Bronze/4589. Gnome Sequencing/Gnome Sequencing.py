# 4589 Gnome Sequencing
n = int(input())
print('Gnomes:')
for i in range(n):
    beard_list = list(map(int,input().split()))
    if beard_list == sorted(beard_list) or beard_list == sorted(beard_list,reverse=True):
        print('Ordered')
    else:
        print('Unordered')