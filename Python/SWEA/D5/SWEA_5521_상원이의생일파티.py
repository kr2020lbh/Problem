import sys
sys.stdin = open("input.txt","r")
for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    g = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    visited[1] = 1
    for u in g[1]:
        visited[u] = 1
        for v in g[u]:
            visited[v] = 1
    print("#{} {}".format(t,sum(visited)-1))
