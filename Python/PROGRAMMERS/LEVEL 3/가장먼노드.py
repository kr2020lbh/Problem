def bfs(edge,edges,visited,length,answer):
    cnt = len(edge)
    if cnt == 0:return answer
    Q = edge
    while cnt!=0:
        cnt -= 1
        indexes = Q.pop(0)
        for i in indexes:
            if visited[i] == 0:
                visited[i] = 1
                Q.append(edges[i])
                answer[i] = length
    answer = bfs(Q,edges,visited,length+1,answer)
    return answer

def solution(n, edge):
    edges = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    visited[1] = 1

    for v1,v2 in edge:
        edges[v1].append(v2)
        edges[v2].append(v1)
    answer = bfs([edges[1]],edges,visited,1,[0] * (n + 1))
    return answer.count(max(answer))


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)