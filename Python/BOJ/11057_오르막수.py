dp = [1] * 10
N = int(input())
if N != 1:
    for i in range(1,N):
        tmp = [0] * 10
        for j in range(10):
            tmp[j] = sum(dp[0:j+1])
        dp = tmp[::]
print(sum(dp)%10007)
