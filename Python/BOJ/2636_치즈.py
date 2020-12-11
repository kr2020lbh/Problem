import sys
sys.stdin = open("input.txt","r")

def melting():
    Q = [[0,0]]
    melting_indexes = []
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    while Q:
        r,c = Q.pop()
        for d_r,d_c in [[-1,0],[1,0],[0,-1],[0,1]]:
            dr,dc = r+d_r, c+d_c
            if 0 <= dr < N and 0 <= dc < M and visited[dr][dc] == 0:
                if cheese[dr][dc] == 1:
                    melting_indexes.append([dr,dc])
                else:
                    Q.append([dr,dc])
                visited[dr][dc] = 1
    cnt = 0
    for r,c in melting_indexes:
        cnt += 1
        cheese[r][c] = 0
    return cnt

N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]
cheese_sum = 0
for i in range(N):
    for j in range(M):
        if cheese[i][j] == 1:
            cheese_sum += 1
time = 1
while True:
    deleted_cheese = melting()
    cheese_sum -= deleted_cheese
    if cheese_sum == 0:
        print(time)
        print(deleted_cheese)
        break
    time += 1
