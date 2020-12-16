import sys
sys.stdin = open("input.txt","r")
def bfs():
    global time
    visited = [[0]* N for _ in range(N)]
    i,j,me = baby[0],baby[1],baby[2]
    visited[i][j] = 1
    Q = [[i,j,0]]
    res = []
    while Q:
        i,j,step = Q.pop(0)
        if maps[i][j] != 0 and maps[i][j] < me:
            res.append([i,j,step])

        for k in range(4):
            di, dj = delta[k][0], delta[k][1]
            d_i = i + di
            d_j = j + dj
            if 0<= d_i < N and 0<= d_j < N and not visited[d_i][d_j] and maps[d_i][d_j] <= me :
                visited[d_i][d_j] = 1
                Q.append([d_i,d_j,step+1])
    if res:
        res.sort(key=lambda x:(x[2],x[0],x[1]))
        i,j,step = res[0]
        maps[i][j] = 9
        maps[baby[0]][baby[1]] = 0
        baby[0], baby[1] = i, j
        baby[3] += 1
        if baby[2] == baby[3]:
            baby[2] += 1
            baby[3] = 0
        time += step
        return True
    return False


N = int(input())
maps = []
flag = True
for i in range(N):
    row = list(map(int,input().split()))
    maps.append(row)
    if flag:
        for j in range(N):
            if row[j] == 9:
                baby = [i,j,2,0]
                flag = False
delta = [[-1,0],[0,-1],[1,0],[0,1]]
time = 0

while bfs():
    pass
print(time)