import sys
sys.stdin = open("input.txt","r")


def bfs():
    Q.append(S)
    visited[S] = 1
    pop_idx = 0
    last_idx = 1
    while pop_idx!=last_idx:
        v = Q[pop_idx]
        pop_idx+=1
        for w in linked[v]:
            if visited[w]==0:
                Q.append(w)
                last_idx+=1
                visited[w] = visited[v]+1


def max_idx(arr):
    MAX = 0
    for i in range(len(arr)):
        if arr[i]>=MAX:
            MAX_IDX=i
            MAX = arr[i]
    return MAX_IDX


for t in range(1,11):

    N,S = map(int,input().split())
    line = list(map(int,input().split()))
    linked = [[] for i in range(101)]
    visited = [0]*101
    Q = []
    for i in range(N//2):
        linked[line[i*2]].append(line[i*2+1])
    bfs()
    print("#{} {}".format(t,max_idx(visited)))
