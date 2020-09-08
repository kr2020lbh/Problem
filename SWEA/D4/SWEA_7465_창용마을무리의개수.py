import sys
sys.stdin = open("input.txt","r")

def f(idx):
    global cnt
    cnt+=1
    Q = []
    Q.extend(arr[idx])
    visited[idx] = 1
    while Q:
        v = Q.pop(0)
        if visited[v] != 1 and arr[v]!=[]:
            Q.extend(arr[v])
            visited[v] = 1


for t in range(1,int(input())+1):
    cnt = 0
    N,M = map(int,input().split())
    arr = [[] for _ in range(N+1)]
    visited  = [0]*(N+1)

    for i in range(M):
        tmp = list(map(int,input().split()))
        arr[tmp[0]].append(tmp[-1])
        arr[tmp[-1]].append(tmp[0])

    for i in range(1,N+1):
        if visited[i] == 0:
            f(i)

    print("#{} {}".format(t,cnt))