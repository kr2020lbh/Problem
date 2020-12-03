import sys,copy
sys.stdin = open("input.txt","r")

def get_breaking_order(cur,depth):
    if depth == N:
        perm.append(cur)
    else:
        for i in range(W):
            get_breaking_order(cur+[i],depth+1)


def fall_down(changing_indexes,bricks):

    for r,c in changing_indexes:
        bricks[r][c] = 0

    for j in range(W):
        new_col = []
        for i in range(H-1,-1,-1):
            if bricks[i][j] != 0:
                new_col.append(bricks[i][j])
        new_col += [0]*(H-len(new_col))
        for i in range(H-1,-1,-1):
            bricks[i][j] = new_col[-i-1]
    return bricks

def breaking_bricks(bricks,breaking_order,depth):
    global min_brick
    visited = [[0]*W for _ in range(H)]
    if min_brick == 0: return
    if depth == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if bricks[i][j] != 0:
                    cnt += 1
        if min_brick > cnt :
            min_brick = cnt
        return

    j = breaking_order[depth]
    for i in range(H):
        if bricks[i][j] != 0:
            Q = [[i, j]]
            visited[i][j] = 1
            changing_indexes = [[i, j]]
            while Q:
                cur_r, cur_c = Q.pop()
                break_range = bricks[cur_r][cur_c]
                if break_range == 1: continue
                for k in range(4):
                    for s in range(1, break_range):
                        dr = cur_r + d_r[k] * s
                        dc = cur_c + d_c[k] * s
                        if 0 <= dr < H and 0 <= dc < W and not visited[dr][dc] and (bricks[dr][dc] != 0):
                            visited[dr][dc] = 1
                            changing_indexes.append([dr, dc])
                            if bricks[dr][dc] > 1:
                                Q.append([dr, dc])
            breaking_bricks(fall_down(changing_indexes, bricks), breaking_order, depth + 1)
            break
    else:
        breaking_bricks(bricks,breaking_order,depth+1)

for t in range(1,int(input())+1):
    N,W,H = map(int,input().split())
    bricks = [list(map(int,input().split())) for _ in range(H)]
    d_r = [-1,1,0,0]
    d_c = [0,0,-1,1]
    perm = []
    get_breaking_order([],0)
    min_brick = W*H
    for p in perm:
        new_bricks = copy.deepcopy(bricks)
        breaking_bricks(new_bricks,p,0)
    print("#{} {}".format(t,min_brick))
