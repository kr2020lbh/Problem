import sys
sys.stdin = open("input.txt","r")

from collections import deque

def make_group_match_condition(r,c,flag):
    Q = deque()
    Q.append([r,c])
    indexes = [[r,c]]
    sumation = nations[r][c]
    while Q:
        r,c = Q.popleft()
        for k in range(4):
            dr = r + d_r[k]
            dc = c + d_c[k]
            if 0 <= dr < N and 0 <= dc < N:
                if visited[dr][dc]==0:
                    if L <= abs(nations[r][c]-nations[dr][dc]) <= R:
                        visited[dr][dc]=flag
                        indexes.append([dr,dc])
                        Q.append([dr,dc])
                        sumation+=nations[dr][dc]
    return indexes,sumation

def do_migrations_match_flag(flag_indexes,flag_sumation):
    for i in range(len(flag_indexes)):
        sumation = flag_sumation[i]
        count = len(flag_indexes[i])
        for j in range(len(flag_indexes[i])):
            r,c=flag_indexes[i][j]
            nations[r][c] = sumation//count



N,L,R = map(int,input().split())
nations = [list(map(int,input().split())) for _ in range(N)]
d_r = [-1,0,1,0]
d_c = [0,1,0,-1]
ans = 0

while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0
    flag_indexes = []
    flag_sumation = []
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                flag += 1
                visited[r][c] = flag
                indexes,sumation = make_group_match_condition(r,c,flag)
                flag_indexes.append(indexes)
                flag_sumation.append(sumation)

    if flag == N**2:
        break

    do_migrations_match_flag(flag_indexes,flag_sumation)
    ans += 1

print(ans)