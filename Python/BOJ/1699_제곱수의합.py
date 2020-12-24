import sys
sys.stdin = open("input.txt","r")
N = int(input())
dp = [0] * 100001
for i in range(1, N + 1):
    dp[i] = i
    j = 1
    while j**2 <= i:
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
        j += 1
print(dp[N])