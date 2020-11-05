import sys
sys.stdin = open("input.txt", "r")

def dijkstra(s):
    U = [s]

    for i in range(V+1):
        D[i] = edges[s][i]

    while len(U) != V:
        for w in range(V+1):
            if w not in U:
                break
        U.append(w)
        for i in range(V+1):
            D[i] = min(D[i],D[w]+edges[w][i])

    return D[-1]

for t in range(1,int(input())+1):
    V,E = map(int,input().split())
    edges = [[99]*(V+1) for _ in range (V+1)]
    for _ in range(E):
        u,v,weight = map(int, input().split())
        edges[u][v]=weight
    D = [99] * (V+1)
    print("#{} {}".format(t,dijkstra(0)))


