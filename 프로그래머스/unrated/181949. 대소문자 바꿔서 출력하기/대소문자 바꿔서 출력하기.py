str = input()
sol =[]
for i in str:
    if i==i.upper():
        i=i.lower()
        sol.append(i)
    else:
        i=i.upper()
        sol.append(i)
print(''.join(sol))