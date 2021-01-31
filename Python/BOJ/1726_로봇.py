import sys
sys.stdin = open("input.txt", "r")
def zero_one_switch(number):
    if number == '1':
        return 0
    else:
        return 1
delta = {
    #상 좌 우 하
    3 : [-1,0],
    1 : [0,-1],
    0 : [0,1],
    2 : [1,0]
    }


N,M = map(int,input().split())
maps = [list(map(zero_one_switch,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

sx,sy,sd = list(map(int,input().split())) 
ex,ey,ed = list(map(int,input().split()))
answer = 1000000
visited[sx-1][sy-1] = True
Q = [[sx-1,sy-1,(sd-1)%4]]
nx, ny =sx-1, sy-1
while Q:
    print()
    [print(m) for m in maps]
    nx,ny,ndir = Q.pop(0)
    cur = maps[nx][ny]
    for d in (0,-1,1,2):
        cdir = (ndir + d) % 4
        print(abs(d),cdir)
        next_x,next_y =  nx + delta[cdir][0], ny + delta[cdir][1]

        if 0<= next_x < N and 0<= next_y < M and maps[next_x][next_y] != 0:  
            if visited[next_x][next_y] == False:
                maps[next_x][next_y] += (cur+abs(d))
                visited[next_x][next_y] = True
                Q.append([next_x,next_y,cdir])
            else:
                if maps[next_x][next_y] > cur+abs(d):
                    
print()
[print(m) for m in maps]



    


