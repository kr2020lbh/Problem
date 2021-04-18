import sys
sys.stdin = open("input.txt","r")

from itertools import combinations

def bfs(maps,viruses):
    time = 1
    while viruses:
        virus = viruses.pop(0)
        spread = []
        for ci,cj in virus:
            if time != 1 and maps[ci][cj] == -2:
                visited[ci][cj] = 1 
            else:
                visited[ci][cj] = time
            for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni,nj = ci+di,cj+dj
                if ni < 0 or ni >=N:
                    continue
                if nj < 0 or nj >=N:
                    continue
                if visited[ni][nj] == 0:
                    visited[ni][nj] = time
                    if maps[ni][nj] == -3 or  maps[ni][nj] == -2:
                        spread.append([ni,nj])

        if spread:
            viruses.append(spread)
        time += 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and maps[i][j] != -1:
                return False
    return visited


def check(visited,maps):
    max_time = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] != -1 and max_time < visited[i][j]:
                max_time = visited[i][j]
    return max_time


N,M = map(int,input().split())
maps = []
indexes = []
ans = 10**5

for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        if row[j] == 2: #바이러스
            indexes.append([i,j])
            row[j] = -2
        if row[j] == 1: #벽
            row[j] = -1

        if row[j] == 0: #빈공간
            row[j] = -3
    maps.append(row)

for comb in combinations(indexes,M):
    visited = [[0]*N for _ in range(N)]
    tmp = [] 
    for i in range(N):
        tmp.append(maps[i][::])
    res = bfs(tmp,[list(comb)])
    if res:
        tmp_time = check(res,tmp)
        if ans > tmp_time:
            ans = tmp_time

if ans == 10**5:
    print(-1)
else:
    print(ans-1)