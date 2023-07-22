# 21300 Bottle Return
bottles_list = list(map(int,input().split()))
total_price = []

for bottle in bottles_list:
    total_price.append(bottle * 5)
print(sum(total_price))