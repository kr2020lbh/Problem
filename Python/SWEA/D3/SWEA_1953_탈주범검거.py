import sys
sys.stdin = open("input.txt","r")
# 1

def bfs(time):
    while time:
        tmp = []
        time -= 1
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 1:
                    d_row,d_col = pipes[str(path[i][j])]
                    for k in range(len(d_row)):
                        dr = d_row[k] + i
                        dc = d_col[k] + j
                        if 0<= dr < N and 0<= dc < M and path[dr][dc] != 0 and visited[dr][dc] == 0:
                            if pipes[str(path[dr][dc])][0][k-2] or pipes[str(path[dr][dc])][1][k-2]:
                                tmp.append([dr,dc])
        for x,y, in tmp:
            visited[x][y] = 1

pipes = {
    #좌 상 우 하
    '1' : [[0,-1,0,1],[-1,0,1,0]],
    '2' : [[0,-1,0,1],[0,0,0,0]],
    '3' : [[0,0,0,0],[-1,0,1,0]],
    '4' : [[0,-1,0,0],[0,0,1,0]],
    '5' : [[0,0,0,1],[0,0,1,0]],
    '6' : [[0,0,0,1],[-1,0,0,0]],
    '7' : [[0,-1,0,0],[-1,0,0,0]]
}
for t in range(1,int(input())+1):
    N,M,row,col,time = map(int,input().split())
    path = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    visited[row][col] = 1
    bfs(time-1)
    res = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                res += 1
    print("#{} {}".format(t,res))
