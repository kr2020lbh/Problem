import sys
sys.stdin = open("input.txt","r")

def get_child(p):
    ttmp = []
    for node in tree[p]:
        if visited[node]==0:
            ttmp.append(node)
            visited[node] = 1
            parent[node] = p
    return ttmp

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0]*(N+1)
visited = [0]*(N+1)
visited[0] = 1
cnt = 1
for i in range(N-1):

    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

S = get_child(1)
while S:
    tmp = []
    for s in S:
        tmp.extend(get_child(s))
    S = tmp

[print(a) for a in parent[2::]]