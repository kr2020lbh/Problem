import sys
from collections import deque

sys.stdin = open("input.txt","r")
def bfs():

    while len(indexes) != 0:
        locate = indexes.popleft()
        row,col,height = locate[0],locate[1],locate[2]
        for i in range(6):

            d_r = row + d_row[i]
            d_c = col + d_col[i]
            d_h = height + d_height[i]
            if 0<= d_r < N and 0<= d_c < M and 0<=d_h<H and box[d_h][d_r][d_c] == 0:
                indexes.append([d_r,d_c,d_h])
                box[d_h][d_r][d_c] = box[height][row][col]+1

    return box[height][row][col]


def check():
    ans = bfs()
    for height in box:
        for row in height:
            if 0 in row:
                print(-1)
                return
    if ans == 1:
        print(0)
    else:
        print(ans-1)

d_row = [-1,1,0,0,0,0]
d_col = [0,0,-1,1,0,0]
d_height = [0,0,0,0,-1,1]
M,N,H = map(int,input().split())
box = []
indexes = deque()
for h in range(H):
    box.append([])
    for n in range(N):
        box[-1].append(list(map(int,input().split())))
        for m in range(M):
            if box[h][n][m] == 1:
                indexes.append([n,m,h])

check()