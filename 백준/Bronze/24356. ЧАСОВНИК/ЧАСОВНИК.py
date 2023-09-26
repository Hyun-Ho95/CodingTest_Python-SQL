# 24356 ЧАСОВНИК(시계)
t1, m1, t2, m2 = map(int,input().split())
start_time = (t1*60) + m1
end_time = (t2*60) + m2

if end_time - start_time <0: 
    end_time += 24*60 
result = end_time-start_time
print(result, result//30)