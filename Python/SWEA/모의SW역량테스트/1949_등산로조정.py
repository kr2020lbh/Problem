import sys
sys.stdin = open("input.txt","r")

def dfs(r,c,work,depth):
    global ans
    if depth > ans:
        ans = depth
    for i in range(4):
        dr,dc = r+d_r[i], c+d_c[i]
        if 0<= dr < N and 0<= dc < N :

            if visited[dr][dc]:
                continue

            if work == 1:
                if maps[dr][dc] < maps[r][c]:
                    visited[dr][dc] = 1
                    dfs(dr,dc,1,depth+1)
                    visited[dr][dc] = 0
            else:
                if maps[dr][dc] < maps[r][c]:
                    visited[dr][dc] = 1
                    dfs(dr,dc,0,depth+1)
                    visited[dr][dc] = 0
                else:
                    for k in range(1,K+1):
                        maps[dr][dc] -= k
                        if maps[dr][dc] < maps[r][c]:
                            visited[dr][dc] = 1
                            dfs(dr,dc,1,depth+1)
                            visited[dr][dc] = 0
                        maps[dr][dc] += k

d_r = [-1,0,1,0]
d_c = [0,1,0,-1]

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    max_height_indexes = []
    max_height = 0
    maps = []

    for i in range(N):
        row = list(map(int,input().split()))
        maps.append(row)
        for j in range(N):
            if row[j] > max_height:
                max_height = row[j]

    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_height:
                max_height_indexes.append([i,j])
    ans = 0
    for r,c in max_height_indexes:
        visited = [[0]*N for _ in range(N)]
        visited[r][c] = 1
        dfs(r,c,0,0)
    print("#{} {}".format(t,ans+1))