import sys
sys.stdin = open("input.txt","r")

def dfs():
    cnt = -1
    while len(stack)!=0:
        v = stack.pop()
        if v not in visited:
            cnt+=1
            visited.append(v)
            for w in range(1,V+1):
                if arr[v][w] == 1 and w not in visited:
                    stack.append(w)
    return cnt


V = int(input())
E = int(input())
arr = [[0]*(V+1) for _ in range(V+1)]
visited = []
stack = []

for i in range(E):
    n1,n2 = map(int,input().split())
    arr[n1][n2]=arr[n2][n1]=1

stack.append(1)

print(dfs())

