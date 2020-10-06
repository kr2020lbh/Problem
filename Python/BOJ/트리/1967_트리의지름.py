import sys
sys.stdin = open("input.txt","r")


def get_far_vertex(vertex):
    visited= [0] *(V+1)
    visited[vertex]=1
    Q=[[vertex,0]]
    max_length = 0
    max_node = vertex
    while Q:
        v,d = Q.pop(0)
        for node in tree[v]:
            if visited[node[0]]==0:
                visited[node[0]] = 1
                Q.append([node[0],node[1]+d])
                if max_length < node[1]+d:
                    max_length = node[1]+d
                    max_node = node[0]
    return [max_node,max_length]


V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(V-1):
    v1,v2,weight = map(int,input().split())
    tree[v1].append([v2,weight])
    tree[v2].append([v1,weight])

print(get_far_vertex(get_far_vertex(1)[0])[1])