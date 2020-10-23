dp = [1] * 10
dp[0] = 0
N = int(input())
if N != 1:
    for i in range(1,N):
        tmp = [0] * 10
        # 0은 1에서 온다
        tmp[0] = dp[1]
        # 9는 8에서 온다
        tmp[9] = dp[8]
        # 1부터 8은 양 옆에서 온다
        for j in range(1,9):
            tmp[j] = dp[j-1]+dp[j+1]
        dp = tmp[::]
print(sum(dp)%1000000000)