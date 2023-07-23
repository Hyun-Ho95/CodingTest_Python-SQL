# 24736 미식축구
away_score = list(map(int,input().split()))
home_score = list(map(int,input().split()))
score_list = [6,3,2,1,2]
away_total_score = 0
home_total_score = 0

for i, score in enumerate(away_score):
    away_total_score += score * score_list[i]
for k, score in enumerate(home_score):
    home_total_score += score * score_list[k]
    
print(away_total_score, home_total_score)