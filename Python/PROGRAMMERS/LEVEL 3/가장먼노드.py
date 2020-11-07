def bfs(edges):
    visited = [0]*len(edges)
    visited[1] = 1
    Q = edges[1]
    while Q:
        length = len(Q)
        tmp = set()
        for u in Q:
            if visited[u] == 0:
                visited[u] = 1
        for u in Q:
            for v in edges[u]:
                if visited[v] == 0:
                    tmp.add(v)
        Q = list(tmp)
    return length

def solution(n, edge):
    edges = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    visited[1] = 1

    for v1,v2 in edge:
        edges[v1].append(v2)
        edges[v2].append(v1)
    return bfs(edges)


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)