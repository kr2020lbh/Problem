def solution(n, money):
    money.sort()
    dp = [0] * 100001
    dp[0] = 1
    for m in money:
        for i in range(1,n+1):
            if i-m >= 0:
                dp[i] += dp[i-m]
    return dp[n] % 1000000007


solution(5,[1,2,5])