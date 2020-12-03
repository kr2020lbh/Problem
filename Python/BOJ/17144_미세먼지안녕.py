import sys
sys.stdin = open("input.txt","r")

def dust_diffusion():
    diffusion_indexes = []
    for r in range(R):
        for c in range(C):
            if maps[r][c] > 1:
                cnt = 0
                divied_dust = maps[r][c]//5
                if divied_dust == 0:
                    continue
                for i in range(4):
                    dr = r + d_r[i]
                    dc = c + d_c[i]
                    if 0<= dr < R and 0<= dc < C:
                        if maps[dr][dc] != -1:
                            cnt += 1
                            diffusion_indexes.append([dr,dc,divied_dust])
                maps[r][c] = maps[r][c] - divied_dust * cnt

    for r,c,dust in diffusion_indexes:
        maps[r][c] += dust

    if len(diffusion_indexes) == 0:
        return False
    return True


def up_air_flow():
    r,c = air_cleaner[0]
    dr,dc = r-1,c
    while dr != 0:
        maps[dr][dc] = maps[dr-1][dc]
        dr -= 1
    while dc != C-1:
        maps[dr][dc] = maps[dr][dc+1]
        dc += 1
    while dr != r:
        maps[dr][dc] = maps[dr+1][dc]
        dr += 1
    while dc != c+1:
        maps[dr][dc] = maps[dr][dc-1]
        dc -= 1
    maps[r][c+1] = 0


def down_air_flow():
    r,c = air_cleaner[1]
    dr,dc = r+1,c
    while dr != R-1:
        maps[dr][dc] = maps[dr+1][dc]
        dr += 1
    while dc != C-1:
        maps[dr][dc] = maps[dr][dc+1]
        dc += 1
    while dr != r:
        maps[dr][dc] = maps[dr-1][dc]
        dr -= 1
    while dc != c+1:
        maps[dr][dc] = maps[dr][dc-1]
        dc -= 1
    maps[r][c+1] = 0

R,C,T = map(int,input().split())
air_cleaner = []
maps = []
d_r = [-1,0,1,0]
d_c = [0,1,0,-1]
maps = [list(map(int,input().split())) for _ in range(R)]

for i in range(R):
    row = maps[i]
    for j in range(C):
        if row[j] == -1:
            air_cleaner.append([i,j])
            break
    if air_cleaner:
        air_cleaner.append([i+1,j])
        break



flag = True
while T:
    if flag:
        flag = dust_diffusion()
    up_air_flow()
    down_air_flow()
    T -= 1
res = 0
for r in range(R):
    for c in range(C):
        if maps[r][c] > 0:
            res += maps[r][c]
print(res)


