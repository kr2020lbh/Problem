import sys
sys.stdin = open("input.txt","r")
N = int(input())
dp = []; money_list = []; day_list = []
for _ in range(N):
    a,b = map(int,input().split())
    day_list.append(a)
    money_list.append(b)
dp = [0] * (N+1)
for i in range(N-1,-1,-1):
    if day_list[i] + i <= N:
        dp[i] = max(money_list[i] + dp[i+day_list[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(max(dp))
