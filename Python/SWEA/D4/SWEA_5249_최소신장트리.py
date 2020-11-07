import sys
sys.stdin = open("input.txt", "r")
def findSet(x):
    while x != p[x]:
        x = p[x]
    return x

def unionSet(x,y):
    p[findSet(y)] = findSet(x)

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    p = [i for i in range(N+1)]
    edges = [list(map(int,input().split())) for _ in range(M)]
    edges.sort(key=lambda x:x[-1])
    res = 0
    for x,y,weight in edges:
        if findSet(x) != findSet(y):
            unionSet(x,y)
            res += weight
    print("#{} {}".format(t,res))

