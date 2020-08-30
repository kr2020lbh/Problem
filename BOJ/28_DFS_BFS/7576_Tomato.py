from collections import deque
import sys

sys.stdin = open("input.txt","r")

def bfs():

    while len(indexes) != 0:
        locate = indexes.popleft()
        row,col = locate[0],locate[1]
        for i in range(4):
            d_r = row + d_row[i]
            d_c = col + d_col[i]
            if 0<= d_r < N and 0<= d_c < M and box[d_r][d_c] == 0:
                indexes.append([d_r,d_c])


                box[d_r][d_c] = box[row][col]+1

    return box[row][col]



M,N = map(int,input().split())

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
box = []
indexes = deque()
queue = []
for row in range(N):
    line = list(map(int,input().split()))
    for col in range(M):
        if line[col]==1:
            indexes.append([row, col])
    box.append(line)

ans = bfs()
for line in box:
    if 0 in line:
        print(-1)
        break
else:print(ans)