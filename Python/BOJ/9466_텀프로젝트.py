import sys
sys.stdin = open("input.txt","r")

def dfs(start,target):
    global ans
    visited[target] = 1
    if visited[B[target]] == 1:
        if start != B[target]:
            ans += 1
    else:
        dfs(start,B[target])


for t in range(int(input())):
    N = int(input())
    B = list(map(int,input().split()))
    B = [0] + B
    visited = [0] * (N+1)
    ans = 0
    for i in range(1,N+1):
        if i == B[i]:
            visited[i] = 1

    for i in range(1, N + 1):
        if visited[B[i]] == 1:
            if i != B[i]:
                visited[i] = 1
                ans += 1
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i,B[i])
    print(ans)
# ###############################
#
# import sys
# sys.stdin = open("input.txt","r")
#
# sys.setrecursionlimit(10**6)
# input = lambda : sys.stdin.readline().strip()
#
# def make_group(x, cnt, start): # start은 시작정점
#     print(cycle_count)
#     # 탐색할수록 정점의 개수(cnt)는 늘어간다.
#     # nexted 배열에 탐색할때마다 해당 정점을 기준으로 탐색된 정점의 개수를 저장한다.
#
#     while True:
#         if cycle_count[x] != False: # 방문 이미 한 곳
#             if start != started[x]: # 정점 시작점이 다를 경우 사이클 x
#                 return 0
#             return cnt - cycle_count[x]
#             # 그러던 중 사이클이 존재하면, 사이클이 존재하는 정점을 인덱스로 활용하는 것이다.
#             # (탐색된 정점 개수 - 사이클 정점에 대한 길이)를 통해 사이클을 이루는 정점의 개수를 구하게 된다.
#
#         cycle_count[x] = cnt
#         started[x] = start
#         x = nexted[x]
#         cnt += 1
#
# for _ in range(int(input())):
#     n = int(input())
#     cycle_count = [False]*(n+1)
#     # cycle_count는 x에 도착했을 때 탐색한 개수를 저장하는 곳
#     # started는 x가 어디에서 시작했는지를 알려주는 곳
#
#     nexted = {}
#     # x의 연결된 위치 알려주는 곳
#     started = [0]+list(map(int, input().split()))
#     for i in range(1, n+1):
#         nexted[i] = started[i]
#
#     ans = 0
#     for i in range(1, n+1):
#         if cycle_count[i] == False:
#             ans += make_group(i, 1, i);
#     print(n-ans)
#
#
# ########################
# # import sys
# # testcase = int(sys.stdin.readline())
# # for _ in range(testcase):
# #     n = int(sys.stdin.readline())
# #     choice = [0] + list(map(int, sys.stdin.readline().split()))
# #     visit = [0] * (n+1)
# #     group = 1
# #     for i in range(1, n+1):
# #         if visit[i] == 0:
# #             while visit[i] == 0:
# #                 visit[i] = group
# #                 i = choice[i]
# #                 while visit[i] == group: visit[i] = -1
# #                 i = choice[i]
# #                 group += 1
# #                 cnt = 0
# #                 for v in visit:
# #                     if v > 0:
# #                         cnt += 1
# #                         sys.stdout.write("{}\n".format(cnt))
