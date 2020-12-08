import sys,copy
sys.stdin = open("input.txt","r")
def check(r,c):
    minus_cnt = 0
    for d_r,d_c in delta:
        dr = r + d_r
        dc = c + d_c
        if 0 <= dr < N and 0<= dc < M:
            if maps[dr][dc] == 0:
                minus_cnt += 1
    return minus_cnt


def connected(indexes):
    visited = [[0] * M for _ in range(N)]
    for key,val in indexes.items():
        r,c = val
        break
    Q = [[r,c]]
    visited[r][c] = 1
    visited_cnt = 1
    while Q:
        r,c = Q.pop(0)
        for d_r,d_c in delta:
            dr = r + d_r
            dc = c + d_c
            if not (0<= dr < N and 0<= dc < M):continue
            if maps[dr][dc] != 0 and not visited[dr][dc]:
                visited[dr][dc] = 1
                Q.append([dr,dc])
                visited_cnt += 1
    if len(indexes) == visited_cnt:
        return True
    return False

def melting():
    time = 0
    while indexes:
        tmp_indexes = []

        for r,c in indexes:
            minus = check(r,c)
            tmp_indexes.append([r,c,minus])

        if not connected(indexes):
            return time


        for r,c,minus in tmp_indexes:
            maps[r][c] -= minus
            if maps[r][c] <= 0:
                maps[r][c] = 0
                del indexes[(r,c)]
        time += 1
    return 0

delta = [[-1,0],[1,0],[0,1],[0,-1]]
N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
indexes = dict()
for i in range(N):
    for j in range(M):
        if maps[i][j] != 0:
            indexes[(i,j)] = (i,j)
print(melting())