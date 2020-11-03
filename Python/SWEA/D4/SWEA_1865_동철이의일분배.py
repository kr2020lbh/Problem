import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = 1 << N
    dp = [[0.0 for _ in range(M)] for _ in range(N)]

    G = []
    for i in range(N):
        G.append(list(map(float, input().split())))
        for j in range(N):
            G[i][j] = G[i][j] / 100
    for i in range(N):
        dp[0][1 << i] = G[0][i]
    print(G)
    print(dp)
    for i in range(1, N):
        for cur in range(1, M):
            if dp[i - 1][cur] == 0:
                continue

            for j in range(N):
                if cur & (1 << j) != 0 or G[i][j] == 0:
                    continue
                next = cur | (1 << j)

                dp[i][next] = max(dp[i][next], dp[i - 1][cur] * G[i][j])
    print("#%d %.6f" % (test_case, dp[N - 1][M - 1] * 100))

# def DFS(flag, idx, value):
#     global ans
#     if flag == (1 << N) - 1:
#         if ans < value * 100:
#             ans = value * 100
#         return
#         # 진행할 수록 값이 작아지니 이미 구한 값보다 작다면 필요없다.
#     if value * 100 <= ans:
#         return
#
#     for i in range(N):
#         # 해당 일은 이미 배정되어서 처리함.
#         if flag & (1 << i): continue
#         print(flag & 1<<i,bin(flag | 1<<i), flag, 1<<i, bin(flag),bin(1<<i))
#         DFS(flag | 1 << i, idx + 1, value * (work[idx][i] / 100))
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     work = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     #flag, idx, value
#     DFS(0, 0, 1)
#     print("#{} {:.6f}".format(tc, ans))

# def f(idx,cursum):
#     global MAX
#
#     if MAX >= cursum:
#         return
#
#     if idx == N-1:
#         MAX = cursum
#
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 f(idx+1,cursum*arr[idx+1][i]/100)
#                 visited[i] = 0
#
#
#
# for t in range(1,int(input())+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     visited = [0]*N
#     MAX = 0
#     for i in range(N):
#         visited[i] = 1
#         f(0,arr[0][i]/100)
#         visited[i] = 0
#     print("#{} {:6f}".format(t,round(MAX*100,6)))