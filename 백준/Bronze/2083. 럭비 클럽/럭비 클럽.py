# 2083 럭비클럽


while True:
    
    name, age, weight = map(str,input().split())
    age,weight = int(age),int(weight)
    
    if name == '#' or age==0:
        break
    else:
        if (age > 17) or (weight >=80):
            print(f'{name} Senior')
        else:
            print(f'{name} Junior')