import sys
sys.stdin = open("input.txt","r")


def dfs(visited, direction, desserts):
    global  ans
    if direction == -1: #처음 시작
        next_direction = [0]
    elif direction ==3: #지금 좌상 그러면 좌상만 가능
        next_direction =[3]
    else:next_direction = [direction,direction+1]
    '''
    direction == 0: #지금 우상, 그러면 우상 or 우하 가능
         next_direction = [0,1]
    direction == 1: #지금 우하, 그러면 우하 or 좌하 가능
         next_direction = [1,2]
    direction == 2: #지금 좌하, 그러면 좌하 or 좌상 가능
         next_direction = [2,3]
    '''
    cur_r,cur_c = visited[-1]
    for next_d in next_direction:
        next_r, next_c = cur_r + d_r[next_d], cur_c + d_c[next_d]
        if 0<= next_r < N and 0<= next_c < N:
            if visited[0] == [next_r,next_c]:
                if ans < len(visited):
                    ans = len(visited)
                    continue

            d = stores[next_r][next_c]
            if desserts[d] != 0:
                continue

            desserts[d] = 1
            dfs(visited+[[next_r,next_c]],next_d,desserts)
            desserts[d] = 0


for t in range(1,int(input())+1):
    N = int(input())
    stores = [list(map(int,input().split())) for _ in range(N)]
    #우상 우하 좌하 좌상
    d_r = [-1,1,1,-1]
    d_c = [1,1,-1,-1]
    ans = -1
    desserts = [0]*101
    for i in range(N):
        for j in range(N):
            desserts[stores[i][j]] = 1
            dfs([[i,j]],-1,desserts)
            desserts[stores[i][j]] = 0

    print("#{} {}".format(t,ans))


# def f(i, j, k, n):  # k: 방향, n:진행한 칸 수
#     global si
#     global sj
#     global maxV
#     if i == si and j == sj:  # 출발점에 도착한 경우
#         if maxV < n:
#             maxV = n
#     elif i < 0 or i >= N or j < 0 or j >= N:
#         return
#     elif cafe[i][j] in v:  # 숫자가 겹치는 경우
#         return
#     elif k == 2 and maxV > 2 * n:
#         return
#     else:
#         v.append(cafe[i][j])
#         if k == 0 or k == 1:  # 오른쪽 아래로 또는 왼쪽 아래로 가는 경우
#             # k 방향으로 계속 가거나r
#             f(i + di[k], j + dj[k], k, n + 1)
#             # k+1 방향으로 전환
#             f(i + di[k + 1], j + dj[k + 1], k + 1, n + 1)
#         elif k == 2:
#             if i + j != si + sj:  # 출발점을 향할 때가 아니면 직진
#                 f(i + di[2], j + dj[2], k, n + 1)
#             else:
#                 f(i + di[3], j + dj[3], k + 1, n + 1)
#         else:  # k==3 직진
#             f(i + di[3], j + dj[3], k, n + 1)
#
#         v.remove(cafe[i][j])
#
#
# di = [1, 1, -1, -1]
# dj = [1, -1, -1, 1]
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     cafe = [list(map(int, input().split())) for i in range(N)]
#     maxV = -1
#     v = []
#     for i in range(N):
#         for j in range(1, N - 1):
#             si = i
#             sj = j
#             v.append(cafe[i][j])
#             f(i + 1, j + 1, 0, 1)
#             v.remove(cafe[i][j])
#     print('#{} {}'.format(tc, maxV))