import sys
sys.stdin = open("input.txt","r")

def dfs(cur_node,visited_nodes,cur_length):
    for i in range(1,V+1):
        if arr[cur_node][i] !=0 and i not in visited_nodes:
            dfs(i,visited_nodes+[i],cur_length+arr[cur_node][i])

    ans.append(cur_length)



V = int(input())
arr = [[0]*(V+1) for _ in range(V+1)]
for i in range(V):
    connections = list(map(int,input().split()))
    V1 = connections[0]
    for j in range((len(connections)-2)//2):
        print(V1,j,j*2,j*2+1)
        arr[V1][connections[j*2+1]] = connections[j*2+2]

ans = []
dfs(1,[],0)
print(max(ans))