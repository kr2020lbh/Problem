import sys
sys.stdin = open("input.txt","r")

def bfs(r,c):
    Q = [[r,c]]
    groups = [[r,c]]
    visited[r][c] = 1
    if not maps[r][c]:
        return []
    while Q:
        nr,nc = Q.pop(0)
        for dr,dc in delta:
            _dr,_dc = nr+dr,nc+dc
            if 0>_dr or _dr >= row:
                continue
            if 0>_dc or _dc >= row:
                continue
            if visited[_dr][_dc]:
                continue
            if not maps[_dr][_dc]:
                continue
            visited[_dr][_dc] = 1
            Q.append([_dr,_dc])
            groups.append([_dr,_dc])
    return groups


def check(r,c):
    cnt = 0
    for dr,dc in delta:
        _dr,_dc = r+dr,c+dc
        if 0>_dr or _dr >= row:
            continue
        if 0>_dc or _dc >= row:
            continue
        if maps[_dr][_dc] > 0:
            cnt += 1
    if cnt > 2:
        return True
    return False


def rot(r,c,size):
    r_start,r_end = r,r+size
    c_start,c_end = c,c+size
    tmp = []
    for i in range(r_start,r_end):
        tmp.append(maps[i][c_start:c_end])
    tmp = list(zip(*tmp[::-1]))
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            maps[i+r_start][j+c_start] = tmp[i][j]


delta = [[0,1],[1,0],[0,-1],[-1,0]]
N,Q = map(int,input().split())
row,col = 2**N,2**N
maps = []
for _ in range(row):
    maps.append(list(map(int,input().split())))
L = list(map(int,input().split()))


for l in L:
    size = 2**l
    if size > 1:
        for r in range(0,row,size):
            for c in range(0,col,size):
                rot(r,c,size)

    indexes = []

    for r in range(row):
        for c in range(col):
            if maps[r][c] == 0:
                continue
            flag = check(r,c)
            if not flag:
                indexes.append([r,c])

    for r,c in indexes:
        maps[r][c] -= 1


ans = [0,0]
for i in range(row):
    ans[0] += sum(maps[i])

visited = [[0]*row for _ in range(row)]
for r in range(row):
    for c in range(col):
        if not visited[r][c]:
            groups = bfs(r,c)
            ans[1] = max(ans[1],len(groups))
            
print(ans[0])
print(0) if ans[1] == 1  else print(ans[1])