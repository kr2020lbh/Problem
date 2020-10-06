import sys
from collections import deque
sys.stdin = open("input.txt","r")

def dfs(cur_node,cur_length):
    global MAX
    for v in arr[cur_node]:
        if v[0]<cur_node:continue
        if visited_nodes[v[0]]==0:
            visited_nodes[v[0]]=1
            dfs(v[0],cur_length+v[1])
            visited_nodes[v[0]]=0
    if cur_length > MAX:
        MAX = cur_length


def bfs(v):
    visited_nodes = [0] * (100001)
    visited_nodes[v] = 1
    MAX = 0
    Q.append([v,0])
    while Q:
        V,D = Q.popleft()
        for vertex in arr[V]:
            if visited_nodes[vertex[0]] == 0:
                visited_nodes[vertex[0]] = 1
                Q.append([vertex[0],D+vertex[1]])
                if MAX < D+vertex[1]:
                    MAX = D+vertex[1]
                    MAX_node = vertex[0]
    return [MAX_node,MAX]


N = int(input())
arr = [[] for _ in range(N+1)]

for i in range(N):
    connections = list(map(int,input().split()))
    V1 = connections[0]
    for j in range((len(connections)-2)//2):
        arr[V1].append([connections[j*2+1],connections[j*2+2]])

for i in arr:
    if i:
        start = i[0][0]
        Q = deque()
        far_node = bfs(start)[0]
        Q = deque()
        print(bfs(far_node)[1])
        break

else:print(0)

