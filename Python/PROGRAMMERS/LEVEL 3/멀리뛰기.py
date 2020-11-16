def solution(n):
    dp = [0] * 2001
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%1234567

for i in range(1,10):
    print(i,solution(i))