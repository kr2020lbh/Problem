import sys
sys.stdin = open("input.txt","r")
from itertools import permutations
# def select():
#     MAX = -1
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0 and works[i][j] > MAX:
#                 MAX = works[i][j]
#                 idx = [i,j]
#     return idx

# def select(cur_idx,visited,sumation):
#     if cur_idx == N:
#         print(sumation)
#     else:
#         if cur_idx == N-1:
#             for i in range(N):
#                 if i not in visited:
#                     select(cur_idx+1,visited+[i],sumation*works[cur_idx][i]/100)
#         else:
#             possible = []
#             for i in range(N):
#                 if i not in visited:
#                     for j in range(N):
#                         if j not in visited+[i]:
#                             possible.append([i,j,works[cur_idx][i]*works[cur_idx+1][j]])
#
#             possible.sort(key=lambda x:-x[2])
#             # print(possible)
#             select(cur_idx+1,visited+[possible[0][0]],sumation*works[cur_idx][possible[0][0]]/100)

def select(cur,visited,sumation):
    global MAX
    if sumation*100 <= MAX:
        return
    if cur == N:
        MAX = sumation*100
    else:
        for i in range(N):
            if i not in visited:
                select(cur+1,visited+[i],sumation*works[cur][i]/100)
for t in range(1,int(input())+1):
    N = int(input())
    works = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    MAX = 0
    select(0,[],1)

    print("#{}".format(t),end=' ')
    print('%.6f' % round(MAX,6))
