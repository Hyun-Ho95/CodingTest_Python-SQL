# 28249 Chill Peppers
pepper_scoville = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}

n = int(input())
cnt = 0
for _ in range(n):
    pepper = input()
    cnt += pepper_scoville[pepper]
print(cnt)