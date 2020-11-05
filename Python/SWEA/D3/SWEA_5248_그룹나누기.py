import sys
sys.stdin = open("input.txt", "r")
def findSet(x):
    Q = []
    while x!=p[x]:
        Q.append(x)
        x = p[x]
    for v in Q:
        p[v] = x
    return x
def unionSet(x,y):
    p[findSet(y)] = findSet(x)


for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    p = [i for i in range(N)]
    arr = list(map(int,input().split()))
    for i in range(M):
        x,y=arr[i*2]-1,arr[i*2+1]-1
        if findSet(x) != findSet(y):
            unionSet(x,y)
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt +=1
    print("#{} {}".format(t,cnt))