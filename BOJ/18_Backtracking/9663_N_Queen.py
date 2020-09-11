N = 4
def check_diagonal(depth,col):
    for i in range(depth):
        if abs(depth - i) == abs(col - visited[i]):
            return False
    return True
def f(depth):
    global cnt
    if depth == N-1:
        cnt+=1
        print(visited)
    else:
        for col in range(N):
            if col in visited:
                continue
            if check_diagonal(depth,col)==False:
                continue


            visited[depth+1] = col
            f(depth+1)
            visited[depth+1] = -1
visited = [0]*N
cnt=0
visited=[-1]*N
for i in range(N):
    visited[0]=i
    f(0)
    visited[0]=-1
print(cnt)