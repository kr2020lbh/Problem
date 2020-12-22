import sys
sys.stdin = open("input.txt","r")
N,C = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
dp = [0] * (C+1)
dp[0] = 1
for c in coins:
    for i in range(c,C+1):
        dp[i] += dp[i-c]
print(dp[-1])
