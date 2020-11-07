import sys,math
sys.stdin = open("input.txt", "r")
def get_min(U,D):
    MIN = math.inf
    for i in range(N):
        if i not in U:
            if D[i] <= MIN:
                MIN = D[i]
                idx = i
    return idx


def dijkstra(s,edges,D):
    U = [s]
    for i in range(N+2):
        D[i] = edges[s][i]
    while len(U) != N:
        print(U)
        w = get_min(U,D)
        U.append(w)
        for j in range(N+2):
            D[j] = min(D[j],D[w] + edges[w][j])
    print(U)
for t in range(1,int(input())+1):
    N = int(input())
    tmp = list(map(int,input().split()))
    locations = []
    for i in range(N+2):
        locations.append([tmp[i*2],tmp[i*2+1]])
    locations[1],locations[-1] = locations[-1],locations[1]
    print(locations)
    edges = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if j != i:
                edges[i][j] = abs(locations[i][0]-locations[j][0]) + abs(locations[i][1]-locations[j][1])

    D = [math.inf] * (N+2)
    dijkstra(0,edges,D)
    print(D)