import sys
sys.stdin = open("input.txt","r")

def bfs():
    cnt = 0
    while len(queue) != 0:
        locate = queue.pop(0)
        row,col = locate[0],locate[1]
        if [row,col] not in visited:
            visited.append([row,col])
            for i in range(4):
                d_r = row + d_row[i]
                d_c = col + d_col[i]
                if maze[d_r][d_c] == 1 and [d_r,d_c] not in visited:
                    queue.append([d_r,d_c])
                    maze[d_r][d_c] += maze[row][col]


N,M = map(int,input().split())
visited = []
queue = []
d_row = [0,1,-1,0]
d_col = [1,0,0,-1]
maze = [[0]*(M+2) for _ in range(N+2)]
cnts = []
for i in range(N):
    maze[i+1][1:M+1] = list(map(int,input()))
queue.append([1,1])
bfs()
for line in maze:
    print(line)
print(maze[N][M])