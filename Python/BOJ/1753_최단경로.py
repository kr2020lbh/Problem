import sys,heapq
sys.stdin = open("input.txt","r")

def dijkstar(start):
    heapq.heappush(Q,[0,start])
    while Q:
        print(Q)
        u_weight,u = heapq.heappop(Q)
        for v,v_weight in path[u]:
            tmp = u_weight + v_weight
            if tmp < dist[v]:
                dist[v] = tmp
                heapq.heappush(Q,(tmp,v))

input = sys.stdin.readline
V,E = map(int,input().split())
start = int(input())
Q = []
path = [[] for _ in range(V+1)]
inf = sys.maxsize
dist = [inf]*(V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    path[u].append((v,w))

dist[start]=0
dijkstar(start)
for i in range(1,V+1):
    print(dist[i] if dist[i] != inf else "INF")