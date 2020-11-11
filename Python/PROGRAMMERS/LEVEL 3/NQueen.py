def dfs(visited,depth,n):
    global answer
    if len(visited) == n:
        answer += 1
    else:
        for i in range(n):
            if i not in visited and check(visited,i,depth+1):
                dfs(visited+[i],depth+1,n)


def check(visited,col,row):
    for i in range(len(visited)):
        if abs(i-row) == abs(visited[i]-col):
            return False
    return True


answer = 0
def solution(n):
    for i in range(n):
        dfs([i],0,n)
    return answer
