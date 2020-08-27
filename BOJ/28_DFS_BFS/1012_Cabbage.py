import sys
sys.stdin = open("input.txt","r")
def dfs(row,col):
    stack.append([row, col])
    while len(stack)!=0:
        locate = stack.pop(0)
        row,col = locate[0],locate[1]
        arr[row][col]=0
        if arr[row-1][col]==1 and visited[row-2][col-1]==0:
            stack.append([row-1,col])
            visited[row-2][col-1]=1

        if arr[row+1][col]==1 and visited[row][col-1]==0:
            stack.append([row+1,col])
            visited[row][col-1]=1

        if arr[row][col-1]==1 and visited[row-1][col-2]==0:
            stack.append([row,col-1])
            visited[row-1][col-2]=1

        if arr[row][col+1]==1 and  visited[row-1][col]==0:
            stack.append([row,col+1])
            visited[row-1][col]=1


stack = []
for t in range(1,int(input())+1):
    M,N,K = map(int,input().split())
    arr = [[0]*(M+2) for _ in range(N+2)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        col,row = map(int,input().split())
        arr[row+1][col+1] = 1
    for i in range(1,N+1):
        for j in range(1,M+1):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt+=1
    print(cnt)
