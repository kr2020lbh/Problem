import sys
sys.stdin = open("input.txt","r")
N = int(input())
dp = [0] * 1000001
dp[1] = dp[2] = 1
for i in range(3,N+1):
    a=b=100000
    if dp[i] == 0:
        if i%3==0:
            a = dp[i//3]
        if i%2==0:
            b = dp[i//2]
        dp[i] = min(a,b,dp[i-1])+1

print(dp[N])