import sys
sys.stdin = open("input.txt","r")
def shark_move():
    tmp = []
    global  cnt
    for i in sharks:
        if i < 0: continue
        r,c = locations[i]
        move = moves[i][directions[i]-1]
        for d in move:
            _dr,_dc = delta[d-1]
            dr,dc = r + _dr , c + _dc
            if 0<= dr < N and 0<= dc < N:
                if smells[dr][dc] == 0:
                    tmp.append([dr,dc,i])
                    directions[i] = d
                    locations[i] = dr,dc
                    break
        else:
            for d in move:
                _dr, _dc = delta[d - 1]
                dr, dc = r + _dr, c + _dc
                if 0 <= dr < N and 0 <= dc < N:
                    shark,k = smells[dr][dc]
                    if shark == i:
                        tmp.append([dr, dc, i])
                        directions[i] = d
                        locations[i] = dr, dc
                        break
    for r,c,shark in tmp:
        if smells[r][c]!=0:
            _shark,k = smells[r][c]
            if _shark == shark:
                smells[r][c] = [shark, K+1]
            else:
                if shark < _shark:  # _shark 사라짐
                    smells[r][c] = [shark, K+1]
                    sharks[_shark] = -1
                else:  # shark 사라짐
                    sharks[shark] = -1
                cnt -= 1
        else:
            smells[r][c] = [shark,K+1]
    for i in range(N):
        for j in range(N):
            if smells[i][j]!=0:
                shark,k = smells[i][j]
                if k == 1:
                    smells[i][j] = 0
                else:
                    smells[i][j] = [shark,k-1]


N,M,K = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
smells = [[0] * N for _ in range(N)]
locations = [[] for _ in range(M)]
delta = [[-1,0],[1,0],[0,-1],[0,1]]
sharks = [i for i in range(M)]
cnt = M
for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            smells[i][j] = [maps[i][j]-1,K]
            locations[maps[i][j]-1] = [i,j]

directions = list(map(int,input().split()))

moves = []
for _ in range(M):
    move = []
    for _ in range(4):
        move.append(list(map(int,input().split())))
    moves.append(move)

res = 0
while cnt > 1:
    if res >=1000:
        res = -1
        break
    shark_move()
    res += 1
print(res)
