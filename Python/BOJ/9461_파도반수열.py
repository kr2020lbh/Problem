import sys

sys.stdin = open("input.txt", "r")

N = int(input())

dp = [1] * 101
dp[4] = dp[5] = 2
for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(N):
    print(dp[int(input())])