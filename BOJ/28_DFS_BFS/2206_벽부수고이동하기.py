import sys
sys.stdin = open("input.txt","r")
di = [1,0,-1,0]
dj = [0,1,0,-1]
def dfs(i,j,cnt,wall_break):

    if i == N-1 and j == M-1:
        return
    for k in range(4):
        d_i = i+di[k]
        d_j = j+dj[k]
        if 0<= d_i < N and 0<= d_j < M:
            if (arr[d_i][d_j] != 0) and (arr[d_i][d_j] !=-1):
                continue
            else:
                if arr[d_i][d_j] == -1:

                    if wall_break==True:
                        continue

                arr[d_i][d_j] = cnt
                dfs(d_i, d_j, cnt + 1, True)

def bfs():



N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            arr[i][j] = -1
arr[0][0] = 1
dfs(0,0,1,False)
print(arr[N-1][M-1]-1)

