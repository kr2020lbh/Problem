def f(Q,visited,nodes):
    while Q:
        v = Q.pop(0)
        for w in nodes[v]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v]+1

def solution(n, edge):
    edge.sort(key=lambda x: (x[0], x[1]))
    nodes = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for e in edge:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])
    visited[1] = 1
    f([1], visited, nodes)
    answer = visited.count(max(visited))
    return answer