import sys,copy
sys.stdin = open("input.txt","r")
from itertools import combinations

def remove_enemy(idx):
    Q = [[N-1,idx,1]]
    while Q:
        r,c,d = Q.pop(0)
        if d <= D:
            if maps[r][c] == 1:
                return (r,c)
            for i in range(3):
                dr = r + d_r[i]
                dc = c + d_c[i]
                if 0<= dr and 0<= dc < M:
                    Q.append([dr,dc,d+1])


def gravity(maps):
    for col in range(M):
        new_col = []
        for row in range(N-1):
            new_col.append(maps[row][col])
        new_col = [0] + new_col
        for row in range(N):
            maps[row][col] = new_col[row]


N,M,D = map(int,input().split())
origin_maps = [list(map(int,input().split())) for _ in range(N)]
d_r = [0,-1,0]
d_c = [-1,0,1]
ans = []
for archers in combinations(range(M),3):
    maps = copy.deepcopy(origin_maps)
    res = 0
    for _ in range(N):
        cnt = dict()
        tmp1 = remove_enemy(archers[0])
        tmp2 = remove_enemy(archers[1])
        tmp3 = remove_enemy(archers[2])
        if tmp1:
            cnt[tmp1] = 1
            maps[tmp1[0]][tmp1[1]] = 0
        if tmp2:
            cnt[tmp2] = 1
            maps[tmp2[0]][tmp2[1]] = 0
        if tmp3:
            cnt[tmp3] = 1
            maps[tmp3[0]][tmp3[1]] = 0
        gravity(maps)
        res += (len(cnt))
    ans.append(res)
print(max(ans))

