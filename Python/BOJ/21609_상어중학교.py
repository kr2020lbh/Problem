import sys
sys.stdin = open("input.txt","r")

def isGroupExist():
    for i in range(N):
        for j in range(N):
            pivotBlock = maps[i][j]
            if pivotBlock == -1 or pivotBlock == -2 or pivotBlock == 0:
                continue
            for di,dj in around:
                ni,nj = i + di, j + dj
                if 0<= ni < N and 0<= nj < N:
                    nearBlock = maps[ni][nj]
                    if nearBlock == pivotBlock or nearBlock == 0:
                        return True
    return False


def findGroup(i,j):
    visited = [[False] * N for _ in range(N)]
    Q = [[i,j]]
    toDelete = [[i,j,maps[i][j]]]
    blockCnt = 0
    pivotBlock = maps[i][j]
    visited[i][j] = True
    rainbowCnt = 0

    while Q:
        _i,_j = Q.pop()
        blockCnt += 1
        for di,dj in around:
            ni,nj = _i + di, _j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
                nearBlock = maps[ni][nj]
                if nearBlock == pivotBlock or nearBlock == 0:
                    if nearBlock == 0:
                        rainbowCnt += 1
                    visited[ni][nj] = True
                    Q.append([ni,nj])
                    toDelete.append([ni,nj,nearBlock])
    toDelete.sort(key=lambda x:(x[0],x[1]))
    for i,j,k in toDelete:
        if k == 0:
            continue
        else:
            return blockCnt,rainbowCnt,i,j,toDelete
    return False

def gravity():
    for i in range(N-1,-1,-1):
        for j in range(N):

            if maps[i][j] == -1 or maps[i][j] == -2:
                continue

            for _i in range(i+1,N):
                if maps[_i][j] == -2:
                    maps[_i-1][j] , maps[_i][j] = maps[_i][j] , maps[_i-1][j]
                else:
                    break


def rot():
    rotMaps = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-1,-1,-1):
            rotMaps[N-1-j][i] = maps[i][j]
    return rotMaps


around = [[-1,0],[0,1],[1,0],[0,-1]]

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
score = 0
while isGroupExist():
    toDelete = []
    blockCnt = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == -1 or maps[i][j] == -2 or maps[i][j] == 0:
                continue
            res = findGroup(i,j)
            if res:
                toDelete.append(res)

    toDelete.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3]))

    delete = toDelete[0]
    score += delete[0]**2
    for di,dj,k in delete[-1]:
        maps[di][dj] = -2

    gravity()
    maps = rot()
    gravity()

print(score)




