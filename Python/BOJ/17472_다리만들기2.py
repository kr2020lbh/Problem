import sys
sys.stdin = open("input.txt","r")

def get_branch(row_length,col_length,arr):
    for r in range(row_length):
        c = 0
        while c < col_length:
            if arr[r][c] != 0:
                start = arr[r][c]
                idx = c + 1
                while idx < col_length:
                    if arr[r][idx] != start:
                        break
                    idx += 1
                zero = idx
                while zero < col_length:
                    if arr[r][zero] != 0:
                        end = arr[r][zero]

                        if zero - idx > 1:
                            d = zero - idx
                            if start > end:
                                start, end = end, start
                            if findSet(start) != findSet(end):
                                unionSet(start, end)
                            if edges[start][end] > d:
                                edges[start][end] = d
                                edges[end][start] = d
                        c = zero - 1
                        break
                    zero += 1
            c += 1

def makeSet(x):
    p[x] = x
def findSet(x):
    Q = []
    while p[x] != x:
        Q.append(x)
        x = p[x]
    for y in Q:
        p[y] = x
    return x


def unionSet(x,y):
    p[findSet(y)] = findSet(x)

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 1
delta = [[-1,0],[1,0],[0,-1],[0,1]]
for r in range(N):
    for c in range(M):
        if maps[r][c] != 0 and visited[r][c] == 0:
            Q = [[r,c]]
            while Q:
                cur_r,cur_c = Q.pop(0)
                visited[cur_r][cur_c] = 1
                maps[cur_r][cur_c] = cnt
                for _dr,_dc in delta:
                    next_r,next_c = cur_r + _dr, cur_c + _dc
                    if 0<= next_r < N and 0<= next_c < M and maps[next_r][next_c] != 0 and visited[next_r][next_c]== 0:
                        Q.append([next_r,next_c])
            cnt += 1

edges = [[1000] * cnt for _ in range(cnt)]

p = [0]*cnt
[makeSet(x) for x in range(cnt)]
# [print(m) for m in maps]
# print()
get_branch(N,M,maps)
col_maps = list(map(list,zip(*maps)))
# [print(c) for c in col_maps]
get_branch(M,N,col_maps)
cnt -= 1
visited = [1]
is_connected = set()
for i in range(1,cnt+1):
    is_connected.add(findSet(i))
if len(is_connected) == 1:
    weight = 0 #출력할 최소 가중치
    while len(visited) != (cnt): #방문한 노드 N개라면 반복문 중단
        MIN = 1000
        for u in visited: #방문한 노드들의 인접 노드를 모두 불러온다
            for v in range(1,cnt+1):
                if v not in visited: #방문하지 않은 노드들 중
                    if MIN >= edges[u][v]: #최소 가중치인지 확인
                        MIN = edges[u][v]
                        tmp = v
        visited.append(tmp) #방문 노드에 최소 가중치를 가진 노드를 추가
        weight += MIN
    print(weight)
else:
    print(-1)