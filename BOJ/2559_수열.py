import sys
sys.stdin = open("input.txt","r")

N,K = map(int,input().split())
nums = list(map(int,input().split()))
dp = [0]*N
dp[0] = nums[0]

for i in range(1,N):
    dp[i] = dp[i-1]+nums[i]
MAX = dp[K-1]

for i in range(K,N):
    SUM = dp[i]-dp[i-K]
    if SUM > MAX:
        MAX = SUM

print(MAX)