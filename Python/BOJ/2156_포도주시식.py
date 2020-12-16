import sys
sys.stdin = open("input.txt","r")
N = int(input())
wines = [int(input()) for _ in range(N)]
dp = [0,wines[0]]
if N > 1:
    dp.append(wines[0]+wines[1])
    for i in range(3, N+1):
        drink_now_and_before = dp[i-3] + wines[i-2] + wines[i-1]
        drink_now = dp[i-2] + wines[i-1]
        not_drink = dp[i-1]
        dp.append(max(drink_now,drink_now_and_before,not_drink))
print(dp[-1])