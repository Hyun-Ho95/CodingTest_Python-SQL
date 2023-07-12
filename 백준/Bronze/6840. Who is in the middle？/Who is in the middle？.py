# 6840번 Who is in the middle?
bowls_list = [int(input()) for i in range(3)]
mamas_bowl = sorted(bowls_list)[len(bowls_list)//2]
print(mamas_bowl)