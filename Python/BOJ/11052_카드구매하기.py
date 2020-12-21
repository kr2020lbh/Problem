import sys
sys.stdin = open("input.txt","r")
N = int(input())
costs = list(map(int,input().split()))
dp = [0] * N
dp[0] = costs[0]
for i in range(1,N):
    tmp = []
    for j in range(i):
        tmp.append(dp[j] + costs[i-j-1])
    dp[i] = max(max(tmp),costs[i])
print(dp[-1])