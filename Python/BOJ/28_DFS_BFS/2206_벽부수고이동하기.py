import sys
import copy
sys.stdin = open("input.txt","r")
from collections import deque


def wallbreaker(arr,point):
    arr[point[0]][point[1]] = 0
    return


def dfs(arr,wallbreak,visited):

    while Q:
        point = Q.popleft()
        r,c = point[0],point[1]
        if r==N-1 and c == M-1:
            cnt.append()
            return
        if wallbreak == False:
            dr, dc = r+d_r[i], c+d_c[i]
            if 0<=dr<N and 0<=dc<M and arr[dr][dc] == 0 and visited[dr][dc]==0:
                visited[dr][dc] = 1
                arr[dr][dc] = arr[r][c] - 1
                Q.append([dr,dc])
        else:

        for i in range(4):




d_r = [-1,1,0,0]
d_c = [0,0,-1,1]
visited = [[0] * 1000 for _ in range(1000)]
visited[0][0] = 1
arr = []
indexes = []

N,M = map(int,input().split())


Q = deque()
cnt= []
for i in range(N):
    row = list(map(int,input()))
    arr.append(row)

Q.append([0,0])
