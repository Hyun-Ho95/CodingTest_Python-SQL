# 11948 과목선택

science = []

for _ in range(4):
    x = int(input())
    science.append(x)
science.remove(min(science))
science
e = int(input())
f = int(input())

print(sum(map(int,science)) + max(e,f))
