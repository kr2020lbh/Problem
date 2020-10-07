import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs():

    while Q:
        r,c,wall = Q.popleft()
        for i in range(4):
            dr = r+d_r[i]
            dc = c+d_c[i]
            if 0 <= dr < N and 0 <= dc < M:
                if arr[dr][dc]==0 and visited[dr][dc][wall]==0:
                    visited[dr][dc][wall]=visited[r][c][wall]+1
                    Q.append([dr,dc,wall])
                if wall == 0 and arr[dr][dc] == 1 and visited[dr][dc][1]==0:
                    visited[dr][dc][1]=visited[r][c][wall]+1
                    Q.append([dr,dc,1])


d_r = [-1,1,0,0]
d_c = [0,0,-1,1]
arr = []
Q = deque()
N,M = map(int,input().split())
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
[arr.append(list(map(int,input()))) for _ in range(N)]

Q.append([0,0,0])
visited[0][0][0] =  1

bfs()

if sum(visited[N-1][M-1])==0:
    print(-1)
else:
    if visited[N-1][M-1][0]==0:
        print(visited[N-1][M-1][1])
    elif visited[N-1][M-1][1]==0:
        print(visited[N-1][M-1][0])
    else:
        print(min(visited[N-1][M-1][0],visited[N-1][M-1][1]))
