import sys
sys.stdin = open("input.txt","r")
def dfs():
    while len(stack)!=0:
        v = stack.pop()

        if v not in dfs_visited:
            print(v,end=' ')
            dfs_visited.append(v)
            for w in range(V,0,-1):
                if arr[v][w] == 1 and w not in dfs_visited:
                    stack.append(w)

def bfs():
    while len(queue)!=0:
        v = queue.pop(0)

        if v not in bfs_visited:
            print(v,end=' ')
            bfs_visited.append(v)
            for w in range(1,V+1):
                if arr[v][w] == 1 and w not in bfs_visited:
                    queue.append(w)



V,E,S = map(int,input().split())
arr = [[0]*(V+1) for _ in range(V+1)]
dfs_visited=[]
bfs_visited=[]
stack = [S]
queue = [S]
for i in range(E):
    n1,n2 = map(int,input().split())
    arr[n1][n2]=arr[n2][n1] = 1
dfs()
print()
bfs()



