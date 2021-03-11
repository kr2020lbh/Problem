import sys
sys.stdin = open("input.txt","r")


def get_child(Q):
    next_Q = []
    for q_list in Q:
        for q in q_list:
            visited[q] = 1
            tmp = []
            for next in tree[q]:
                if not visited.get(next):
                    tmp.append(next)
            next_Q.append(tmp)

    return next_Q
tree = {}
visited = {}
N = int(input())
for _ in range(N-1):
    a,b = map(int,input().split())
    if tree.get(a):
        tree[a].append(b)
    else:
        tree[a] = [b]
    if tree.get(b):
        tree[b].append(a)
    else:
        tree[b] = [a]
cnt = 0
Q = [[1]]
while Q:
    print(Q)
    Q = get_child(Q)



M = int(input())
for _ in range(M):
    a,b = map(int,input().split())