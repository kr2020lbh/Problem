import sys
sys.stdin = open("input.txt","r")
delta = [[-1,0], [1,0], [0,-1], [0,1]]
N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
MAX = 0
for rain in range(101):
    cnt,visited = 0,[[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if maps[row][col] > rain and not visited[row][col]:
                cnt += 1
                Q = [[row,col]]
                while Q:
                    i,j = Q.pop(0)
                    for di,dj in delta:
                        ni,nj = i+di,j+dj
                        if 0 > ni or ni >= N:
                            continue
                        if 0 > nj or nj >= N:
                            continue
                        if maps[ni][nj] <= rain:
                            continue
                        if visited[ni][nj]:
                            continue

                        visited[ni][nj] = 1
                        Q.append([ni,nj])

    MAX = cnt if MAX < cnt else MAX

print(MAX)
