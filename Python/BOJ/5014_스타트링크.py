import sys
sys.stdin = open("input.txt","r")
def sol():
    Q = [[S,0]]
    visited[S] = 1
    while Q:
        cur,time = Q.pop(0)
        if cur == G:
            print(time)
            return
        for move in [U,-D]:
            next = cur + move
            if 1 <= next <=G and not visited[next]:
                visited[next] = 1
                Q.append([next,time+1])
    print('use the stairs')

F,S,G,U,D = map(int,input().split())
visited = [0] * (F+1)
sol()
