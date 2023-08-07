def solution(score):
    
    avg_score = [sum(i)/len(i) for i in score]
    sorted_avg_score = sorted(avg_score,reverse=True)
    
    result = [sorted_avg_score.index(i)+1 for i in avg_score]
    return result
