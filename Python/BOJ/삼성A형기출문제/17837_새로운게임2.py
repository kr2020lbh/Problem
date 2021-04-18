import sys
sys.stdin = open("input.txt","r")
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def move(chess_idx):
    r,c,l = chess[chess_idx]
    nr,nc = r+dr[l],c+dc[l]
    if nr < 0 or nr >= N or nc < 0 or nc >= N or maps[nr][nc] == 2:
        if l <2:
            l = (l+1) % 2
        else:
            l = (l-1)%2 + 2
        nr,nc = r+dr[l],c+dc[l]
        chess[chess_idx][2] = l
        if nr < 0 or nr >= N or nc < 0 or nc >= N or maps[nr][nc] == 2:
            return False

    for i in range(len(chess_map[r][c])):
        if chess_map[r][c][i] == chess_idx:
            chess_up = chess_map[r][c][i:]
            chess_map[r][c] = chess_map[r][c][:i]
            break

    if maps[nr][nc] == 1:
        chess_up = chess_up[::-1]

    for idx in chess_up:
        chess_map[nr][nc].append(idx)
        chess[idx][0:2] = [nr,nc]

    if len(chess_map[nr][nc]) >= 4:
        return True
    return False

N,K = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
chess_map = [[[] for _ in range(N)] for _ in range(N)]
chess = [_ for _ in range(K)]

for _ in range(K):
    i,j,k = map(int,input().split())
    chess[_] = [i-1,j-1,k-1]
    chess_map[i-1][j-1].append(_)

cnt = 1
break_flag = False
while cnt <= 1000:
    for i in range(K):
        flag = move(i)
        if flag:
            break_flag = True
            break
    if break_flag:
        break
    cnt += 1
if break_flag:
    print(cnt)
else:
    print(-1)


