import sys,copy
from itertools import combinations
sys.stdin = open("input.txt","r")
d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
def bfs(Q,tmp_arr):

    while Q:
        tmp = []
        for r,c in Q:
            for i in range(4):
                dr,dc  = r+d_row[i], c+d_col[i]
                if 0<= dr < N and 0<= dc < M and tmp_arr[dr][dc] == 0 :
                    tmp.append([dr,dc])
                    tmp_arr[dr][dc] = 2
        Q = tmp[::]

    return get_count(tmp_arr)

def get_count(tmp_arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 0:
                cnt += 1
    return cnt

def num_to_row_col(num):
    r = num // M
    num -= num // M
    c = num % M
    return [r,c]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
zero = []
two = []
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            two.append([i,j])

for comb in combinations(range(N*M),3):
    wall_idx = list(map(num_to_row_col,comb))
    tmp_arr = copy.deepcopy(arr)
    flag = 0

    for i,j in wall_idx:
        if tmp_arr[i][j] == 0:
            tmp_arr[i][j] = 1
            flag += 1

    if flag != 3:continue

    cnt = bfs(two, tmp_arr)

    if cnt > ans:
        ans = cnt

print(ans)
