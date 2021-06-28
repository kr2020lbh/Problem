import sys
sys.stdin = open("input.txt","r")

def move(idx):
    d, p = rains[idx]
    d -= 1
    for i in range(len(clouds)):
        r, c = clouds[i]
        nr = (r + dr[d] * p) % N
        nc = (c + dc[d] * p) % N
        clouds[i] = [nr, nc]
        visited[nr][nc] = True


def rain_drop():
    for i in range(len(clouds)):
        r, c = clouds[i]
        maps[r][c] += 1


def rain_add():
    for i in range(len(clouds)):
        r, c = clouds[i]
        cnt = 0
        for d in [1, 3, 5, 7]:
            _r = r + dr[d]
            _c = c + dc[d]
            if 0 <= _r < N and 0 <= _c < N and maps[_r][_c]:
                cnt += 1
        maps[r][c] += cnt


def new_clouds():
    tmp = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 2 and visited[i][j] == False:
                maps[i][j] -= 2
                tmp.append([i, j])
    return tmp


dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
rains = [list(map(int, input().split())) for _ in range(M)]
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for i in range(M):
    visited = [[False] * N for _ in range(N)]
    move(i)
    rain_drop()
    rain_add()
    clouds = new_clouds()

ans = 0
for i in range(N):
    for j in range(N):
        ans += maps[i][j]
print(ans)