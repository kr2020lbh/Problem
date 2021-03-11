import sys
sys.stdin = open("input.txt","r")


delta = [
    [-1,0],
    [-1,-1],
    [0,-1],
    [1,-1],
    [1,0],
    [1,1],
    [0,1],
    [-1,1]
]

while True:
    W,H = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]

    if W or H:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if maps[i][j] and not visited[i][j]:
                    cnt += 1
                    Q = [[i,j]]
                    while Q:
                        cur_i,cur_j = Q.pop(0)
                        for di,dj in delta:
                            ni,nj = cur_i + di, cur_j + dj
                            if 0<= ni < H and 0<= nj < W and maps[ni][nj] and visited[ni][nj] == 0:
                                visited[ni][nj] = 1
                                Q.append([ni,nj])
        print(cnt)
    else:
        break