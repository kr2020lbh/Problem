# 가성비를 찾는 문제, 칼로리당 점수가 가장 높은 것을 찾는 거다.
#T
# N(재료 수 ) L(칼로리)
# 점수, 칼로리
#
T = int(input())
for t in range(1,T+1):
    N,L = map(int,input().split())
    result_score = 0
    result_cal = 0
    score_cals =  []
    for _ in range(N):
        score,cal = map(int,input().split())
        score_cals.append([score,cal,score/cal])
        
    score_cals.sort(key = lambda x:(-x[2],x[1]))
    
    for score_cal in score_cals:
        result_score += score_cal[0]
        result_cal += score_cal[1]
        
        if result_cal > L:
            result_score -= score_cal[0]
            result_cal -= score_cal[1]
    print(f'#{t} {result_score}')