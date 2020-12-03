import sys
sys.stdin = open("input.txt","r")

def dfs(cost,cur_idx):
    global  min_cost
    if cost > min_cost:
        return
    if cur_idx >= 12:
        if cost < min_cost:
            min_cost = cost
        return

    if plan[cur_idx]:
        dfs(cost + day * plan[cur_idx], cur_idx + 1)
        dfs(cost + one_month, cur_idx + 1)
        dfs(cost + three_month, cur_idx + 3)
    else:
        dfs(cost, cur_idx + 1)


for t in range(1,int(input())+1):
    day,one_month,three_month,one_year = map(int,input().split())
    plan = list(map(int,input().split()))
    DP = [0] * 13
    for i in range(1,13):
        DP[i] = DP[i-1] + min(day*plan[i-1],one_month)
        if i >= 3:
            DP[i] = min(DP[i],DP[i-3]+three_month)
    # dfs(0,0)

    print("#{} {}".format(t,min(DP[12],one_year)))