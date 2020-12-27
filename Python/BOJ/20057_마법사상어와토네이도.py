import sys
sys.stdin = open("input.txt","r")
def get_tornado(d):
    if d == 2:
        tornado = [[-2, 0, 2], [-1, 0, 7], [1, 0, 7], [2, 0, 2], [-1, 1, 1], [1, 1, 1], [-1, -1, 10], [1, -1, 10],
               [0, -2, 5]]
    if d == 0:
        tornado = [[-2, 0, 2], [-1, 0, 7], [1, 0, 7], [2, 0, 2], [-1, -1, 1], [1, -1, 1], [-1, 1, 10], [1, 1, 10],
                   [0, 2, 5]]
    if d == 1:
        tornado = [[0, -2, 2], [0, -1, 7], [0, 1, 7], [0,2, 2], [-1,-1, 1], [-1, 1, 1], [1, -1, 10], [1, 1, 10],
                   [2, 0, 5]]
    if d == 3:
        tornado = [[0, -2, 2], [0, -1, 7], [0, 1, 7], [0, 2, 2], [1, 1, 1], [1, -1, 1], [-1, 1, 10], [-1, -1, 10],
                   [-2, 0, 5]]
    return tornado
N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1
move = 0
d_move = [[0,1],[1,0],[0,-1],[-1,0]]
moves = []
cur_r,cur_c = 0,0
while True:
    next_r,next_c = cur_r + d_move[move][0], cur_c + d_move[move][1]
    if next_r == N//2 and next_c == N//2:
        moves.append([next_r,next_c,(move-2)%4])
        break
    if 0<= next_r < N and 0<= next_c < N and visited[next_r][next_c] == 0:
        visited[next_r][next_c] = 1
        moves.append([next_r,next_c,(move-2)%4])
        cur_r,cur_c = next_r,next_c
    else:
        move = (move+1)%4

moves = moves[::-1]
ans = 0
for move in moves:
    row,col,d = move
    row,col = row + d_move[d][0], col + d_move[d][1]
    dust = maps[row][col]
    cur_dust = maps[row][col]
    for dr,dc,pt in get_tornado(d):
        moved_dust = (dust * pt) // 100
        d_row = row + dr
        d_col = col + dc
        if 0<= d_row < N and 0<= d_col <N:
            maps[d_row][d_col] += moved_dust
            cur_dust -= moved_dust
        else:
            ans += moved_dust
            cur_dust -= moved_dust
    if d == 2 :
        if 0<= col - 1:
            maps[row][col-1] += cur_dust
        else:
            ans += cur_dust
    if d == 0:
        if col + 1 < N:
            maps[row][col+1] += cur_dust
        else:
            ans += cur_dust
    if d == 3:
        if 0<= row - 1:
            maps[row-1][col] += cur_dust
        else:
            ans += cur_dust
    if d == 1:
        if row + 1 < N:
            maps[row + 1][col] += cur_dust
        else:
            ans += cur_dust

    maps[row][col] = 0
print(ans)
