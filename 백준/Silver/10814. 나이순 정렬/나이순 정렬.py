# 10814번 나이순 정렬 (Silver V)
n = int(input())
answer = []

for _ in range(n):
    age,name = input().split()
    answer.append([int(age),name])
answer.sort(key = lambda x : (x[0]))
    
for i in answer:
    print(i[0],i[1])