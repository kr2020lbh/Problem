N = int(input())
def check(depth):
    for i in range(depth+1):
        if visited[depth+1]==visited[i]:
            return False
        if abs(depth+1-i)==abs(visited[depth+1]-visited[i]):
            return False
    else:return True

def f(depth):
    global cnt
    if depth == N-1:
        cnt+=1
    else:
        for col in range(N):
            visited[depth+1]=col
            if check(depth):
                f(depth+1)

visited = [0]*N
cnt=0
for i in range(N):
    visited[0]=i
    f(0)
print(cnt)