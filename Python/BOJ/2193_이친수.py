dp = [1,1]
N = int(input())
if N < 3:
    print(1)
elif N == 3:
    print(2)
else:
    for i in range(N-3):
        dp = [dp[0]+dp[1],dp[0]]
    print(sum(dp))