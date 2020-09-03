import sys
sys.stdin = open("input.txt","r")
def dfs(i,j):
    Q = []
    Q.extend([i,j])

    while Q:
        r,c = Q.pop(0),Q.pop(0)
        if maze[r][c]==3:
            return 1
        maze[r][c] = 1
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if maze[nr][nc] != 1:
                Q.extend([nr,nc])
    return 0


dr = [-1,1,0,0]
dc = [0,0,-1,1]
for t in range(1,11):
    tc = input()
    maze = [ list(map(int,input())) for _ in range(100)]
    print("#{} {}".format(t,dfs(1,1)))